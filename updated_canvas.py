import tkinter as tk
import random

# List of polyatomic ions with names and formulas
ions = [
    {"name": "Ammonium", "formula": "NH₄⁺"},
    {"name": "Acetate", "formula": "C₂H₃O₂⁻ (CH₃COO⁻)"},
    {"name": "Hydroxide", "formula": "OH⁻"},
    {"name": "Hypochlorite", "formula": "ClO⁻"},
    {"name": "Chlorite", "formula": "ClO₂⁻"},
    {"name": "Chlorate", "formula": "ClO₃⁻"},
    {"name": "Perchlorate", "formula": "ClO₄⁻"},
    {"name": "Bromate", "formula": "BrO₃⁻"},
    {"name": "Iodate", "formula": "IO₃⁻"},
    {"name": "Nitrate", "formula": "NO₃⁻"}
]

# Function to select a random ion and display it
def display_random_ion():
    selected_ion = random.choice(ions)
    ion_label.config(text=f"Draw the ion: {selected_ion['name']} ({selected_ion['formula']})")

# Initialize main window
root = tk.Tk()
root.title("Polyatomic Ion Drawing Canvas")

# Display a label for the ion to draw
ion_label = tk.Label(root, text="Click 'New Ion' to start!")
ion_label.pack(pady=10)

# Create the canvas widget
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Variables to store previous mouse position
prev_x, prev_y = None, None

# Function to reset drawing on the canvas
def clear_canvas():
    canvas.delete("all")

# Function to draw line
def draw(event):
    global prev_x, prev_y
    if prev_x and prev_y:
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill="black", width=2)
    prev_x, prev_y = event.x, event.y

# Reset previous coordinates when mouse is lifted
def reset(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None

# Bind mouse events to the canvas
canvas.bind("<B1-Motion>", draw)  # Draw when left mouse button is held down
canvas.bind("<ButtonRelease-1>", reset)  # Reset on mouse release

# Add control buttons
new_ion_button = tk.Button(root, text="New Ion", command=display_random_ion)
new_ion_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
