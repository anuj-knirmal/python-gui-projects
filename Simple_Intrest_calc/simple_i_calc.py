from tkinter import*
win=Tk()
win.geometry("600x400")
win.title("Simple Intrest Calculater")
win.resizable(1,0) 
#---------formula--------
def si():
 p=eval(entn1.get())
 r=int(entn2.get())
 t=int(entn3.get())
 si=p*r*t/100
 res.config(text="Your simple Intrest is:"+str(si))


lebln1=Label(win,text="Enter Principle ammount:",font=("Arial 14 bold"),fg="blue")
lebln1.place(x=15,y=50)

lebln2=Label(win,text="Enter rate of ammount:",font=("Arial 14 bold"),fg="blue")
lebln2.place(x=15,y=100)

lebln3=Label(win,text="Enter time:",font=("Arial 14 bold"),fg="blue")
lebln3.place(x=15,y=150)


#inputs
entn1=Entry(win,font=("Arial 14 bold"))
entn1.place(x=300,y=50)

entn2=Entry(win,font=("Arial 14 bold"))
entn2.place(x=300,y=100)

entn3=Entry(win,font=("Arial 14 bold"))
entn3.place(x=300,y=150)

btn=Button(win,text="Calculate Simple Interest:",font=("Arial 14 bold"),fg="red" , command=si)
btn.place(x=50,y=300)


res=Label(win,text="Your simple Intrest is:",font=("Arial 14 bold"),fg="green")
res.place(x=25,y=250)



win.mainloop()