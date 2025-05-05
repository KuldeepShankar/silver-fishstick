import tkinter
from tkinter import *
from reappearsave import *
from reappearfind import *
from reappearupdate import *
from reappeardelete import *
from reappearshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Reappear Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showreappearsave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showreappearfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showreappearupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showreappeardelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showreappearshow)
bt.place(x=60,y=250)

t.mainloop()