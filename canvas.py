import cv2
import numpy as np

# Initialize webcam (or replace with canvas/frame capturing logic)
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

# Define color ranges for elements (tune these values for your colors)
colors = {
    'Carbon': ([0, 100, 100], [10, 255, 255]),  # Red for Carbon
    'Hydrogen': ([100, 150, 0], [140, 255, 255]),  # Blue for Hydrogen
    'Oxygen': ([40, 100, 100], [70, 255, 255]),  # Green for Oxygen
    'Bond': ([0, 0, 0], [180, 255, 50])  # Black for Bond
}

def detect_elements(frame, hsv):
    detected_elements = []

    for element, (lower, upper) in colors.items():
        lower_np = np.array(lower, dtype='uint8')
        upper_np = np.array(upper, dtype='uint8')
        mask = cv2.inRange(hsv, lower_np, upper_np)
        
        # Find contours for detected colors
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            if radius > 10:  # Avoid noise by filtering small objects
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv2.putText(frame, element, (int(x)-10, int(y)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                detected_elements.append((element, (int(x), int(y))))

    return detected_elements

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Detect elements in the current frame
    elements = detect_elements(frame, hsv)

    # Show the live detection
    cv2.imshow('Live Element Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
