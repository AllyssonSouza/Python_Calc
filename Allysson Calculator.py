import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the entry box
def press(num):
    expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression + str(num))

# Function to evaluate the expression and display the result
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Allysson Calculator")
root.geometry("500x600")

# Entry box for the calculator
entry = tk.Entry(root, width=30, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in a grid
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, height=3, width=8, command=evaluate)
    else:
        btn = tk.Button(root, text=button, height=3, width=8, command=lambda b=button: press(b))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(root, text="Clear", height=3, width=34, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the main application loop
root.mainloop()
