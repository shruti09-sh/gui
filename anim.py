from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.title('Animation')
root.geometry("800x500")

def change(e):
	my_pic= PhotoImage(file="images/m1.png")
	my_label.config(image=my_pic)
	my_label.image = my_pic

def change_back(e):
	my_pic= PhotoImage(file="images/k1.PNG")
	my_label.config(image=my_pic)
	my_label.image = my_pic

def do_something():
	label2 = Label(root, text="You clicked the button!")
	label2.pack()

my_pic = PhotoImage(file="images/k1.PNG")
my_label = Button(root, image=my_pic, command=do_something)
my_label.pack(pady=20)


my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)
root.mainloop()