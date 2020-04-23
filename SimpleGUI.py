from tkinter import *

#Fenetres
def spawnWindow():
	window = Tk()

	#Body
	window.title("LazyPost Minds.com")
	window.geometry('400x500')


	lbl = Label(window, text="Platform", height=2, font=("Helvetica", 16))

	lbl.grid(column=2, row=0)

	def clicked():

	    newLbl = Label(window, text="Go!", height=2, font=("Helvetica", 16))
	    newLbl.grid(column=2, row=2)
		

	btn01 = Button(window, text="Minds",  width=10, height=3, command=clicked)
	btn02 = Button(window, text="Steemit", width=10, height=3, command=clicked)
	btn03 = Button(window, text="Bitchute", width=10, height=3, command=clicked)
	btn04 = Button(window, text="LBRY", width=10, height=3, command=clicked)
	btn05 = Button(window, text="D.Tube", width=10, height=3, command=clicked)

	btn01.grid(column=0, row=1)
	btn02.grid(column=1, row=1)
	btn03.grid(column=2, row=1)
	btn04.grid(column=3, row=1)
	btn05.grid(column=4, row=1)


	window.mainloop()

if __name__== "__main__":
  spawnWindow()