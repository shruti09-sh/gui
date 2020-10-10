from tkinter import *


root = Tk()
root.geometry("400x600")

def something():
	my_label.config(text="this is something", font=("helvetica", 8))
	root.config(bg="blue")
	my_button.config(text="you've been configged", pady=15)

global my_label
my_label = Label(root, text="my text", font=("helvetica", 18))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)

























root.mainloop()

