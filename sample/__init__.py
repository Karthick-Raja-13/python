from tkinter import *

w = Tk()
w.title("Home Page")
w.geometry("500x500")

e = Entry(w)
e.pack()
def showVal():
    print(e.get())
b = Button(text="show",command=showVal)
b.pack()
w.mainloop()
