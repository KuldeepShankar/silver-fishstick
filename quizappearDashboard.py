import tkinter
from tkinter import *
from quizappearsave import *
from quizappearfind import *
from quizappearupdate import *
from quizappeardelete import *
from quizappearshow import *
t=tkinter.Tk()
t.geometry('700x700')

he=Label(t,text='quizappear Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showquizappearsave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showquizappearfind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showquizappearupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showquizappeardelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showquizappearshow)
bt.place(x=60,y=250)

t.mainloop()