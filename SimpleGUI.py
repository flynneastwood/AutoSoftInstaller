from tkinter import *

#Fenetres
window = Tk()

#Body
window.title("LazyPost Minds.com")
window.geometry('350x300')
#Body
window.title("LazyPost Minds.com")
window.geometry('400x500')


lbl = Label(window, text="Send to Minds.com")
lbl = Label(window, text="Platform", height=2, font=("Helvetica", 16))

lbl.grid(column=0, row=0)
lbl.grid(column=2, row=0)

def clickedMinds():

	print('Executing Minds!')

def clickedSteemit():

		print('Executing Steemit!')

def clickedBitchute():

		print('Executing Bitchute!')

def clickedLBRY():

		print('Executing LBRY!')

def clickedDtube():

		print('Executing Dtube!')




btn01 = Button(window, text="Minds",  width=10, height=3, command=clickedMinds)
btn02 = Button(window, text="Steemit", width=10, height=3, command=clickedSteemit)
btn03 = Button(window, text="Bitchute", width=10, height=3, command=clickedBitchute)
btn04 = Button(window, text="LBRY", width=10, height=3, command=clickedLBRY)
btn05 = Button(window, text="D.Tube", width=10, height=3, command=clickedDtube)


btn01.grid(column=0, row=1)
btn02.grid(column=1, row=1)
btn03.grid(column=2, row=1)
btn04.grid(column=3, row=1)
btn05.grid(column=4, row=1)

window.mainloop()

if __name__== "__main__":
  spawnWindow()