from tkinter import *

#Fenetres
window = Tk()

#Body
window.title("LazyPost Minds.com")
window.geometry('350x300')


lbl = Label(window, text="Send to Minds.com")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Go!", command=clicked)

btn.grid(column=1, row=1)

window.mainloop()
