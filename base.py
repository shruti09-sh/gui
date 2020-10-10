from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("This Is My First Window")
root.iconbitmap('camera.ico')

def open():
  global my_img
  top = Toplevel()
  top.title('My Second Window')
  top.iconbitmap('camera.ico')
  my_img = ImageTk.PhotoImage(Image.open("images/yoo1.png"))
  my_label = Label(top, image=my_img).pack()	
  btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
