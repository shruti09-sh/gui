from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("This Is My First Window")
root.iconbitmap('camera.ico')

def open():
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('camera.ico')
	my_img = ImageTk.PhotoImage(Image.open("images/m1.PNG"))
	my_label = Label(top, text="close window", command=top.destroy).pack()

btn2 = Button(top, text="Open Second Window", command=open).pack()

mainloop()
