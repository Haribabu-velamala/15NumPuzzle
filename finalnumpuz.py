import tkinter as tk
import random
from tkinter import messagebox


# Initialize the Tkinter root window
root = tk.Tk()

# Set the window title
root.title("15 Puzzle")

# Set the window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create a list of numbers 1 through 15 and add a 0 to represent the empty space
tiles = list(range(0, 16))
#tiles.append(0)

# Shuffle the list of tiles
random.shuffle(tiles)

# Create the 4x4 grid using nested lists
grid = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
    grid.append(row)


# Populate the grid with the shuffled tiles
for i in range(4):
    for j in range(4):
        grid[i][j] = tiles.pop()

# Define a function to find the coordinates of the empty space (0 tile)
def find_empty_space():
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return (i, j)

# Define a function to handle button clicks
def button_click(row, col):
    # Check if the clicked button is adjacent to the empty space
    empty_row, empty_col = find_empty_space()
    if (row == empty_row and abs(col - empty_col) == 1) or \
       (col == empty_col and abs(row - empty_row) == 1):
        # Swap the clicked button with the empty space
        grid[empty_row][empty_col], grid[row][col] = grid[row][col], grid[empty_row][empty_col]
        # Redraw the grid
        draw_grid()
        # Check if the puzzle is solved
        if is_solved():
            # Display a message box indicating that the puzzle is solved
            messagebox.showinfo("Congratulations!", "You solved the puzzle!")



# Define a function to draw the grid of buttons
def draw_grid():
    # Clear the current grid
    #for child in root.winfo_children():
     #   if isinstance(child, tk.Button):
      #     child.destroy()
    # Loop through the grid and create a button for each tile
    for i in range(4):
        for j in range(4):
            # Create the button with the appropriate text and command
            # Check if the current tile value is not 0
            if grid[i][j] != 0:
    # If it's not 0, convert the value to a string and assign it to the text variable
                text = str(grid[i][j])
            else:
    # If it is 0, assign an empty string to the text variable
                text = ""

            button = tk.Button(root, text=text, width=10, height=5,
                                command=lambda row=i, col=j: button_click(row, col))
            # Place the button in the grid
            button.grid(row=i, column=j, sticky="nsew")

    # Configure column and row weights to make the buttons fill the window
    for i in range(4):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)

# Define a function to check if the puzzle is solved
def is_solved():
    # Create an empty list to store the flattened grid
    flattened_grid = []
    
    # Loop through each row in the grid
    for row in grid:
        # Loop through each value in the row
        for val in row:
            # Add the value to the flattened grid
            flattened_grid.append(val)
    
    # Check if the flattened grid matches the solved state of the puzzle
    solved_state = list(range(1, 16)) + [0]
    return flattened_grid == solved_state


# Draw the initial grid
draw_grid()

# Start the Tkinter event loop
root.mainloop()

