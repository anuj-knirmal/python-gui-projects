from tkinter import *

# Create the main window
win = Tk()
win.geometry("400x550")
win.title("Simple Calculator")
win.configure(bg="#f4f4f4")

# Function to perform addition
def add():
    try:
        n1 = float(entn1.get())
        n2 = float(entn2.get())
        sum = n1 + n2
        res.config(text="Result: " + str(sum), fg="green")
    except ValueError:
        res.config(text="Please enter valid numbers!", fg="red")

# Function to perform subtraction
def sub():
    try:
        n1 = float(entn1.get())
        n2 = float(entn2.get())
        sub = n1 - n2
        res.config(text="Result: " + str(sub), fg="green")
    except ValueError:
        res.config(text="Please enter valid numbers!", fg="red")

# Function to perform multiplication
def mult():
    try:
        n1 = float(entn1.get())
        n2 = float(entn2.get())
        mult = n1 * n2
        res.config(text="Result: " + str(mult), fg="green")
    except ValueError:
        res.config(text="Please enter valid numbers!", fg="red")

# Function to perform division
def div():
    try:
        n1 = float(entn1.get())
        n2 = float(entn2.get())
        if n2 == 0:
            res.config(text="Cannot divide by zero!", fg="red")
        else:
            div = n1 / n2
            res.config(text="Result: " + str(div), fg="green")
    except ValueError:
        res.config(text="Please enter valid numbers!", fg="red")

# Labels
lbln1 = Label(win, text="Enter 1st Number:", font=("Helvetica", 12), bg="#f4f4f4", fg="#4b0082")
lbln1.place(x=20, y=20)

lbln2 = Label(win, text="Enter 2nd Number:", font=("Helvetica", 12), bg="#f4f4f4", fg="#4b0082")
lbln2.place(x=20, y=70)

# Entry fields
entn1 = Entry(win, font=("Helvetica", 14), bd=2, relief="groove", width=20)
entn1.place(x=200, y=20)

entn2 = Entry(win, font=("Helvetica", 14), bd=2, relief="groove", width=20)
entn2.place(x=200, y=70)

# Result label
res = Label(win, text="Result: ", font=("Helvetica", 14, "bold"), fg="red", bg="#f4f4f4")
res.place(x=20, y=130)

# Buttons with modern design and placement
addbtn = Button(win, text=" + ", font=("Helvetica", 16, "bold"), bg="#ff6347", fg="white", relief="raised", width=5, height=2, command=add)
addbtn.place(x=50, y=210)

subbtn = Button(win, text=" - ", font=("Helvetica", 16, "bold"), bg="#ff6347", fg="white", relief="raised", width=5, height=2, command=sub)
subbtn.place(x=150, y=210)

multbtn = Button(win, text=" x ", font=("Helvetica", 16, "bold"), bg="#ff6347", fg="white", relief="raised", width=5, height=2, command=mult)
multbtn.place(x=250, y=210)

divbtn = Button(win, text=" / ", font=("Helvetica", 16, "bold"), bg="#ff6347", fg="white", relief="raised", width=5, height=2, command=div)
divbtn.place(x=300, y=210)

# Start the GUI loop
win.mainloop()
