from tkinter import *

root=Tk()

e=Entry(root,width-50,fg="red",bg="dark green")
e.pack()

def myClick():
	myLabel=Label(root,text="Look!i clicked a button!!")
	myLabel.pack()

myButton=Button(root,text="Click Me!",command=myClick,fg="purple",bg="#f56387")
myButton.pack()

root.mainloop()
