import tkinter as tk
from tkinter import *

root= tk.Tk()
root.geometry("500x500")
root.configure(background="light blue")

def addtoList2():
    curselected=Listbox1.curselection()
    for i in curselected:
        c=Listbox1.get(i)
        Listbox2.insert(END,c)
        Listbox1.delete(tk.ACTIVE)
        
def addtolist1():
    curselected2=Listbox2.curselection()
    for x in curselected2:
        c2=Listbox2.get(x)
        Listbox1.insert(END,c2)
        Listbox2.delete(tk.ACTIVE)
        
def addall_l2():
    for a in range(len(School_Friends)):
        c3=Listbox1.get(a)
        Listbox2.insert(END,c3)
        Listbox1.delete(tk.ACTIVE)
        
def addall_l1():
    for b in range(len(College_Friends)):
        c4=Listbox2.get(b)
        Listbox1.insert(END,c4)
        Listbox2.delete(tk.ACTIVE)
        
School_Friends=["Mujib","Rafik","Aijaz","Adnan","Nadeem","Sarfaraj"]
fav=Label(text="School Friends:", font=('Arial',15),bg="pink", fg="black")
fav.place(x=20,y=20)
Listbox1=Listbox(root,width=20, height=15, fg='white', bg='black' , font=('Arial',15), selectmode='multiple')
Listbox1.place(x=20,y=50)

for i in range (len(School_Friends)):
    Listbox1.insert(END,School_Friends[i])
    


College_Friends=["Afzal","Sakib","Tariq","Danish","Arshi","Ami"]
fav2=Label(text="College Friends:",font=('Arial',15),bg="pink",fg="black")
fav2.place(x=360,y=50)
Listbox2=Listbox(root, width=20, height=15, fg='white', bg='black' , font=('Arial',15), selectmode='multiple')
Listbox2.place(x=360,y=50)

for i in range (len(College_Friends)):
    Listbox2.insert(END,College_Friends[i])
    
btn1=Button(text=">", width=6,height=2,command=addtoList2)
btn1.place(x=280,y=100)

btn2=Button(text="<",width=6,height=2,command=addtolist1)
btn2.place(x=280,y=150)

btn3=Button(text=">>",width=6,height=2,command=addall_l2)
btn3.place(x=280,y=250)

btn4=Button(text="<<",width=6,height=2,command=addall_l1)
btn4.place(x=280,y=300)

root.mainloop()
