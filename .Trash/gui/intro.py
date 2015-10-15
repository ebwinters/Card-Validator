import tkinter

root = tkinter.Tk()

hi_there = tkinter.Label(
	root,
	text="Hi there",
	bg='red',
	fg='white',

	)
hi_there.pack(fill=tkinter.BOTH, expand=True)

my_name = tkinter.Label(root, text="Ethan is my name")
my_name.pack()

root.mainloop()