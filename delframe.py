from tkinter import *

root = Tk()
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

#clickcommand
def our_command():
	my_label = Label(root, text="You Clicked A DropDown Menu").pack()

def file_new():
	hide_all_frames()
	file_new_frame.pack(fill="both", expand=1)
	my_label = Label(file_new_frame, text="You Clicked the File >> New Menu!").pack()


def edit_cut():
	hide_all_frames()
	edit_cut_frame.pack(fill="both", expand=1)
	my_label = Label(edit_cut_frame, text="You Clicked the File >> Cut Menu!").pack()

def edit_copy():
	hide_all_frames()
	edit_copy_frame.pack(fill="both", expand=1)
	my_label = Label(edit_copy_frame, text="You Clicked the File >> Copy Menu!").pack()


def option_find():
	hide_all_frames()
	option_find_frame.pack(fill="both", expand=1)
	my_label = Label(option_find_frame, text="You Clicked the File >> Find Menu!").pack()

def option_find_new():
	hide_all_frames()
	option_find_new_frame.pack(fill="both", expand=1)
	my_label = Label(option_find_new_frame, text="You Clicked the File >> Find New Menu!").pack()
	dummy_button = Button(option_find_new_frame, text="fake!").pack(pady=10)

	child_label = Label(option_find_new_frame, text=option_find_new_frame.winfo_children()[0])
	child_label.pack(pady=10)

	#print(option_find_new_frame.winfo_children())
    #[<tkinter.Label object .!frame5.!label>, <tkinter.Button object .!frame5.!button>, <tkinter.Label object .!frame5.!label2>]

def hide_all_frames():
	#Loop through all the children thru frame and del them
	for widget in file_new_frame.winfo_children():
		widget.destroy()

	for widget in edit_cut_frame.winfo_children():
		widget.destroy()

	for widget in edit_copy_frame.winfo_children():
		wnnnh

	for widget in option_find_frame.winfo_children():
		widget.destroy()

	for widget in option_find_new_frame.winfo_children():
		widget.destroy()


	file_new_frame.pack_forget()
	edit_cut_frame.pack_forget()
	edit_copy_frame.pack_forget()
	option_find_frame.pack_forget()
	option_find_new_frame.pack_forget()



#create menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#create anedit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=edit_copy)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=option_find)
option_menu.add_separator()
option_menu.add_command(label="Find New", command=option_find_new)


file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")
edit_copy_frame = Frame(root, width=400, height=400, bg="purple")
option_find_frame = Frame(root, width=400, height=400, bg="green")
option_find_new_frame = Frame(root, width=400, height=400, bg="brown")





root.mainloop()