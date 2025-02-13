import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

# Function to be called when the button is clicked
def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Image Button Example")

# Load an image using PhotoImage (supports GIF and PNG formats)
#image = PhotoImage(file="path/to/your/image.png")  # Update with your image path

# Create a button with the image
#image_button = tk.Button(root, image=image, command=button_click)
#image_button.pack(padx=10, pady=10)

def press_0():
    print("Button 0 pressed")

root = tk.Tk()

style = ttk.Style()
style.configure("Rounded.TButton", 
                font=('Arial', 20),
                padding=10, 
                borderwidth=1,
                relief="flat",
                anchor="center")

style.map("Rounded.TButton", 
          background=[('active', 'grey28'), ('!active', 'grey38')],
          foreground=[('pressed', 'white'), ('active', 'white')],
          focuscolor=[('!focus', 'grey38')])

Button_Frame = ttk.Frame(root)
Button_Frame.columnconfigure(0, weight=1)
Button_Frame.columnconfigure(1, weight=1)

Btn0 = ttk.Button(Button_Frame, text="0", command=press_0, style="Rounded.TButton")
Btn0.grid(row=0, column=0, sticky=tk.W+tk.E)

Button_Frame.pack(fill = 'x') 
# Start the Tkinter event loop
root.mainloop()


Button_Frame = ttk.Frame(root)
Button_Frame.columnconfigure(0, weight=1)
Button_Frame.columnconfigure(1, weight=1)
