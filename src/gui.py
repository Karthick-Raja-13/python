from tkinter import *
from tkinter import messagebox as mb
w = Tk()
w.title("Home Page")
w.geometry("500x500")
button = Button(text="First")
button2 = Button(text="Second")
btn = Button(text="First BTN")
btn2 = Button(text="Second BTN")
button.grid(row=1,column=1)
button2.grid(row=0,column=1)
btn.grid(row=1,column=0)
btn2.grid(row=0,column=0)
w.mainloop()
'''
val = StringVar(value="Others")
rb1 = Radiobutton(w,text="Male",value="Male",variable=val).pack()
rb2 = Radiobutton(w,text="Female",value="Female",variable=val).pack()
rb3 = Radiobutton(w,text="Others",value="Others",variable=val).pack()
def show():
    #mb.showinfo("Gender",val.get())
    #mb.showwarning("Gender",val.get())
    #mb.showerror("Gender",val.get())
    ans=mb.askyesno("Message","Are You Okay..?")
    ans = mb.askyesnocancel("Message", "Are You Okay..?")
    ans = mb.askokcancel("Message", "Are You Okay..?")
    print(ans)
b = Button(text="Click",command=show).pack()
l = Label(w, text="Hello", bg="black", fg="white", width=40)
l.pack()
l2 = Label(w, text="Hello 2")
l2.pack()
e = Entry(w)
e.pack()
result_label = Label(w, text="")
result_label.pack()
def showval():
    output = e.get()
    result_label.config(text=output)

b = Button(text="Show", command=showval)
b.pack()
from tkinter import *
from tkinter import messagebox as mb
window = Tk()
window.geometry("500x500")
window.title("Tkinter Sample App")
f1 = Frame()
f1.pack()
data = ["Fight Club","One Piece","Demon Slayer"]

lb = Listbox(f1,height=5,width=30)
def showSelected():
    index = lb.curselection()
    print()
def deleteItem():
    index = lb.curselection()
    data.remove(data[index[0]])
    lb.delete(index)
c1_val = BooleanVar()
c2_val = BooleanVar()
c3_val = BooleanVar()
c1 = Checkbutton(w,text="Biryani",variable=c1_val)
c2 = Checkbutton(w,text="Pizza",variable=c2_val)
c3 = Checkbutton(w,text="Burger",variable=c3_val)
c1.pack()
c2.pack()
c3.pack()
def show():
    if c1_val.get():
        print(c1.cget("text"))
    if c2_val.get():
        print(c2.cget("text"))
    if c3_val.get():
        print(c3.cget("text"))
    print("_____________________________________________________")
btn = Button(f1,text="Show",command=showSelected).grid(row=1,column =0)
btn = Button(f1,text="Delete",command=deleteItem).grid(row=1,column =1)
lb.grid(row=0,column =0)

def add():
    for i in data:
        lb.insert(END, i)
add()
lab = Label(window,text="Gender")
lab.pack()
val = StringVar(value="Others")
rb1 = Radiobutton(window,text="Male",value="Male",variable=val).pack()
rb2 = Radiobutton(window,text="Female",value="Female",variable=val).pack()
rb3 = Radiobutton(window,text="Others",value="Others",variable=val).pack()
def showSelected():
    #mb.showinfo(),warning,error
    m =mb.askokcancel("Sample","Are You Okay") #yesno ,yesnocancel
    print(m)
btn = Button(text="Show Selected",command=showSelected)
btn.pack()
c1_check = BooleanVar()
c2_check = BooleanVar()
c3_check = BooleanVar()

ent = Entry(window,width=30,foreground="white",background="black")
ent.pack()
#l.pack()
c1 = Checkbutton(window,text="Biryani",variable=c1_check)
c2 = Checkbutton(window,text="Pizza",variable=c2_check)
c3 = Checkbutton(window,text="Burger",variable=c3_check)
c1.pack()
c2.pack()
c3.pack()
def sayHii():
   user_input = ent.get()
   l2 = Label(window,text=user_input)
   l2.pack()
   ent.delete(0,END)
   if c1_check.get():
      print(c1.cget("text"))
   if c2_check.get():
      print(c2.cget("text"))
   if c3_check.get():
      print(c3.cget("text"))
b = Button(window,text="Click",command=sayHii)
b.place(x=120,y=170)
window.mainloop()
'''
