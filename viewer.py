from tkinter import *
from PIL import ImageTk, Image


root = Tk()


my_img1 = ImageTk.PhotoImage(Image.open("images/a.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/four1.PNG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/i1.PNG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/k1.PNG"))
my_img5 = ImageTk.PhotoImage(Image.open("images/l1.PNG"))
my_img6 = ImageTk.PhotoImage(Image.open("images/j1.PNG"))
my_img7 = ImageTk.PhotoImage(Image.open("images/q1.PNG"))
my_img8 = ImageTk.PhotoImage(Image.open("images/s1.PNG"))
my_img9 = ImageTk.PhotoImage(Image.open("images/u1.PNG"))
my_img10 = ImageTk.PhotoImage(Image.open("images/v1.PNG"))
my_img11 = ImageTk.PhotoImage(Image.open("images/m1.PNG"))
my_img12 = ImageTk.PhotoImage(Image.open("images/o1.PNG"))
my_img13 = ImageTk.PhotoImage(Image.open("images/Cap1.PNG"))
my_img14 = ImageTk.PhotoImage(Image.open("images/anu1.PNG"))





image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12, my_img13, my_img14]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E )

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 14:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E )
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    




def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E )
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


    
button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()







