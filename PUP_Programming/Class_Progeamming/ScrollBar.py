
from tkinter import *

main = Tk()
scroll = Scrollbar(main)
scroll.pack(fill=Y,side=RIGHT)
lb = Listbox(main,yscrollcommand=scroll.set)
for i in range(30):
    lb.insert(END,"Number "+str(i)) 
lb.pack()

scroll.config(command=lb.yview)
main.mainloop()