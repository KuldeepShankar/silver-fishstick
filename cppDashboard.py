import tkinter
from tkinter import *
from cppsave import *
from cppfind import *
from cppupdate import *
from cppdelete import *
from cppshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Python Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showcppsave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showcppfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showcppupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showcppdelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showcppshow)
bt.place(x=60,y=250)

t.mainloop()