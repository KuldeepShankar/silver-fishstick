import tkinter
from tkinter import *
from studentssave import *
from studentsfind import *
from studentsupdate import *
from studentsdelete import *
from studentsshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Student Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showstudentssave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showstudentsfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showstudentsupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showstudentsdelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showstudentsshow)
bt.place(x=60,y=250)

t.mainloop()