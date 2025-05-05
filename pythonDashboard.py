import tkinter
from tkinter import *
from pythonsave import *
from pythonfind import *
from pythonupdate import *
from pythondelete import *
from pythonshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Python Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showpythonsave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showpythonfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showpythonupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showpythondelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showpythonshow)
bt.place(x=60,y=250)

t.mainloop()