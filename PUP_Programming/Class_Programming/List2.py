from select import select
import tkinter as tk
from tkinter import *
from webbrowser import get

root = Tk()
root.geometry("500x500")

def getcourseList():
    selectedCourses=[]
    curselected = lb.curselection()
    for i in curselected:
        c=lb.get(i)
        selectedCourses.append(c)
    print(selectedCourses)
    
# declaring Label
courses = Label(text="Select Course")
courses.pack()
coursesList=['Software Development','Animation','IT IMs','Cuber Security']
lb=Listbox(font=("Arial",10),selectmode=MULTIPLE)
for i in range(len(coursesList)):
    lb.insert(END,coursesList[i])
btn = Button(text="Get Course",command=getcourseList)
btn.pack()
lb.pack()
root.mainloop()