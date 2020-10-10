from tkinter import *

root = Tk()
root.geometry("500x400")

e = Entry(root, width=50)
e.pack(pady=30)

def click():
	my_label = Label(root, text="Hello")
	my_label.pack()



my_button = Button(root, text="click here", command=click)
my_button.pack(pady=10)



root.mainloop()