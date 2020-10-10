from tkinter import *
from PIL import ImageTk, Image
 
root = Tk()
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c =Checkbutton(root, text="would u like a pizza?",variable=var, onvalue="yes", offvalue="no")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()