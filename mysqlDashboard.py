import tkinter
from tkinter import *
from mysqlsave import *
from mysqlfind import *
from mysqlupdate import *
from mysqldelete import *
from mysqlshow import *
t=tkinter.Tk()
t.geometry('700x700')

he=Label(t,text='Mysql Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showmysqlsave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showmysqlfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showmysqlupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showmysqldelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showmysqlshow)
bt.place(x=60,y=250)

t.mainloop()