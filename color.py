from tkinter import *
from tkinter import colorchooser

root = Tk()
root.geometry("400x400")

def color():
	my_color = colorchooser.askcolor()[1]
	my_label = Label(root, text=my_color).pack(pady=10)
	my_label2 = Label(root, text="you picked color", font=("Helvetica, 24"), bg=my_color, fg="white").pack()

my_button = Button(root,text="Pick a Color", command=color).pack()
root.mainloop()