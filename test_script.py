# Example UI with user interaction:

import tkinter as tk

# Create main window to display things in
window = tk.Tk()

# Set window size
window.geometry("600x600")

# Create header label
header_label = tk.Label(window, text="Amy's Sample UI", width=1000, font=("Courier", 40, "bold"))

# Create label asking the user to submit their name
name_label = tk.Label(window, text = "What's your name?", font=('calibre',10, 'bold'))

# Create string variable to store submitted name in
# Create an Entry widget for the user to submit their name
name_var=tk.StringVar()
name_entry = tk.Entry(window, textvariable = name_var, font=('calibre',10,'normal'))

# Define a function to execute when a user submits a name
def submit():
    name=name_var.get()
    print("The name is : " + name)
    display_var.set(f"Hi, {name}! Welcome to my UI")
    name_var.set("")

# Create a button that executes the submit function when clicked
submit_button=tk.Button(window,text = 'Submit', command = submit)

# Create string variable to store string to display
# Set to empty string to start
# Create a label for display string
display_var = tk.StringVar()
display_var.set("")
display_label = tk.Label(window, textvariable = display_var, font=('calibre', 10, 'normal'))

# Create photo image widget to display scientist
scientist_image = tk.PhotoImage(file="images/scientist-beaker-test-tube-animated-f.gif")
scientist_image_label = tk.Label(window, image=scientist_image)

# Create a function to reveal scientist image
def reveal_scientist_image():
    scientist_image_label.pack()

# Create a button to reveal scientist image
reveal_scientist_button=tk.Button(window, text="Reveal scientist", command=reveal_scientist_image)
 
# Place all elements defined above in order using "pack"
header_label.pack()
name_label.pack()
name_entry.pack()
submit_button.pack()
display_label.pack()
reveal_scientist_button.pack()
 
window.mainloop()