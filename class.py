from tkinter import *

root = Tk()
root.geometry("400x400")

class ABC:

	def __init__(self, master):
		myFrame = Frame(master)
		myFrame.pack()

		self.myButton = Button(master, text="Click Me!", command=self.clicker)
		self.myButton.pack(pady=20)


	def clicker(self):
		print("Look at you..you clicked a button!")

a = ABC(root)


root.mainloop()


