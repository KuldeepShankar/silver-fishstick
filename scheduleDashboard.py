import tkinter
from tkinter import *
from schedulesave import *
from schedulefind import *
from scheduleupdate import *
from scheduledelete import *
from scheduleshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Schedule Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showschedulesave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showschedulefind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showscheduleupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showscheduledelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showscheduleshow)
bt.place(x=60,y=250)

t.mainloop()