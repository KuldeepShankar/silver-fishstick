import tkinter
from tkinter import *
from institutesave import *
from institutefind import *
from instituteupdate import *
from institutedelete import *
from instituteshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Institute Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showinstitutesave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showinstitutefind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showinstituteupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showinstitutedelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showinstituteshow)
bt.place(x=60,y=250)

t.mainloop()