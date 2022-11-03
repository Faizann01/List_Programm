
from tkinter import*
import tkinter as tk

from Lable_Demo import submit

root=Tk()
root.geometry("300x200")

W = Label(root,text='Gujarat University', font="50").pack()

Checkbutton1= IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()

Button1 = Checkbutton(root,text ="Tutorial",variable = Checkbutton1, onvalue=1,offvalue=0,height=3,width=10)
Button2 = Checkbutton(root,text ="Student",variable = Checkbutton2, onvalue=1,offvalue=0,height=2,width=10)
Button3 = Checkbutton(root,text ="Course",variable = Checkbutton3, onvalue=1,offvalue=0,height=2,width=10)


                  
Button1.pack()
Button2.pack()
Button3.pack()
sub_btn=Button(root,text='Submit').pack()
root.mainloop()