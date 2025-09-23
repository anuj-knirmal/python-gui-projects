from tkinter import *

# Create the main window
win = Tk()
win.geometry("350x550")
win.title("Temperature Converter")
win.configure(bg="#e0f7fa")  # Soft cyan background

# Function to convert Celsius to Fahrenheit
def c2f():
    try:
        n1 = float(entn1.get())  # Use float for decimal values
        c2f = (9 / 5) * n1 + 32
        res.config(text="Result: {:.2f} °F".format(c2f), fg="green")
    except ValueError:
        res.config(text="Please enter a valid number!", fg="red")

# Function to convert Fahrenheit to Celsius
def f2c():
    try:
        n1 = float(entn1.get())  # Use float for decimal values
        f2c = (n1 - 32) * 5 / 9
        res.config(text="Result: {:.2f} °C".format(f2c), fg="green")
    except ValueError:
        res.config(text="Please enter a valid number!", fg="red")

# Labels
lbln1 = Label(win, text="Enter Temperature:", font=("Helvetica", 14), fg="#00796b", bg="#e0f7fa")
lbln1.place(x=30, y=50)

# Entry field for temperature input
entn1 = Entry(win, font=("Helvetica", 14), fg="blue", bd=2, relief="groove", width=15)
entn1.place(x=170, y=50)

# Result label
res = Label(win, text="Result:", font=("Helvetica", 14, "bold"), fg="#00796b", bg="#e0f7fa")
res.place(x=30, y=150)

# Button to convert Celsius to Fahrenheit
ctof = Button(win, text="C to F", font=("Helvetica", 14, "bold"), fg="white", bg="#00796b", relief="raised", width=10, height=2, command=c2f)
ctof.place(x=30, y=220)

# Button to convert Fahrenheit to Celsius
ftoc = Button(win, text="F to C", font=("Helvetica", 14, "bold"), fg="white", bg="#00796b", relief="raised", width=10, height=2, command=f2c)
ftoc.place(x=180, y=220)

# Start the GUI loop
win.mainloop()
