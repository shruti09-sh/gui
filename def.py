from tkinter import *

root = Tk()
root.geometry("600x400")

my_listbox = Listbox(root, width=50, bg='blue', fg='white')
my_listbox.pack(pady=15)

my_list = ["mon","tue","wed", "mon","tue","wed", "mon","tue","wed"]

for item in my_list:
	my_listbox.insert(END, item)
def select():
	my_label = Label(root, text="gjghf", font=("helvetica", 18))
	my_label.pack()

my_button = Button(root, text="Select Here", command=select)
my_button.pack()

root.mainloop()
	