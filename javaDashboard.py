import tkinter
from tkinter import *
from javasave import *
from javafind import *
from javaupdate import *
from javadelete import *
from javashow import *
t=tkinter.Tk()
t.geometry('700x700')

he=Label(t,text='Java Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showjavasave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showjavafind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showjavaupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showjavadelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showjavashow)
bt.place(x=60,y=250)

t.mainloop()