from tkinter import *
from PIL import ImageTk,Image

root = Tk()

#r=IntVar()
#r.set("2")

TOPPINGS = [("Pepperoni","Pepperoni"),
            ("Cheese","Cheese"),
            ("Mushroom","Mushroom"),
            ("Onions","Onions"),]

pizza = StringVar()
pizza.set = ("Pepperoni")

for text,topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)



def clicked(value):
	myLabel = Label(root,text=value)
	myLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get)).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get)).pack()	

def show():
  c =Checkbutton(root, text="wud u like a pizza?", onvalue=yes, offvalue=no)
  c.deslect()
  c.pack()


myButton = Button(root, text="Show selection", command=show)
myButton.pack()

root.mainloop()


