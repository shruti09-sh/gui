from tkinter import *

root = Tk()
root.geometry("600x400")

def grab():
	my_label.config(text=my_box.get())


my_box = Entry(root, font=("helvetica", 28))
my_box.pack(pady=20)

my_button = Button(root, text="Grab Text From The Box", command=grab)
my_button.pack(pady=20)


my_label = Label(root, text="")
my_label.pack(pady=20)



root.mainloop()