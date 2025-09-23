from tkinter import *
import random

# Create the main window
win = Tk()
win.geometry("700x400")
win.title("Friendship Calculator")
win.configure(bg="#aa8e40")  # Soft pink background

# Function to calculate friendship percentage
def calc():
    name = ent1.get()
    friend_name = ent2.get()
    if name == "" or friend_name == "":
        res.config(text="Please enter both your names.", fg="red")
    else:
        p = random.randint(1, 100)
        res.config(text=f"Friendship Percentage: {p}%", fg="green")

# Header label
label1 = Label(win, text="Check Your Friendship Percentage!", font=("Helvetica", 18, "bold"), fg="#ff6347",)
label1.pack(pady=20)

# Labels for inputs
label2 = Label(win, text="Enter Your Name:", font=("Helvetica", 12, "bold"), fg="#4b0082", bg="#ff99cc")
label2.pack(pady=(0, 10))

label3 = Label(win, text="Enter Your Friend's Name:", font=("Helvetica", 12, "bold"), fg="#4b0082", bg="#ff99cc")
label3.pack(pady=(0, 20))

# Entry fields
ent1 = Entry(win, font=("Helvetica", 14), bd=2, relief="groove", width=25)
ent1.pack(pady=(0, 10))

ent2 = Entry(win, font=("Helvetica", 14), bd=2, relief="groove", width=25)
ent2.pack(pady=(0, 20))

# Button with rounded corners and color effects
btn = Button(win, text="Check Your True Friendship %", font=("Helvetica", 14, "bold"), fg="white", bg="#ff6347", relief="raised", command=calc)
btn.pack(pady=10)
btn.config(width=25, height=2)

# Result label with a larger font for visibility
res = Label(win, text="Result will be shown here", font=("Helvetica", 16, "bold"), fg="#4b0082", bg="#ff99cc")
res.pack(pady=20)

# Start the GUI loop
win.mainloop()
