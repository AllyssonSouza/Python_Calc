import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Aplicativo")
root.geometry("300x200")  # Set window size

# Function to handle button click
numero = 1

def on_button_click():
    global numero
    print("Button clicked!")
    print(numero)   
    if numero < 5:
        numero += 1

# Add a label
label = tk.Label(root, text="Hello, Tkiter!")
label.pack(pady=10)

# Add a button
button = tk.Button(root, text="Apert aquie", command=on_button_click)
button.pack(pady=10)


# Run the application
root.mainloop()
