import tkinter
from tkinter import *
from resulttablesave import *
from resulttablefind import *
from resulttableupdate import *
from resulttabledelete import *
from resulttableshow import *
t=tkinter.Tk()
t.geometry('700x700')


he=Label(t,text='Resulttable Dashboard',fg='red',bg='yellow',font=('arial',30))
he.place(x=170,y=15)

bt=Button(t,text='SAVE',command=showresulttablesave)
bt.place(x=60,y=90)

bt=Button(t,text='FIND',command=showresulttablefind)
bt.place(x=60,y=130)

bt=Button(t,text='UPDATE',command=showresulttableupdate)
bt.place(x=60,y=170)

bt=Button(t,text='DELETE',command=showresulttabledelete)
bt.place(x=60,y=210)

bt=Button(t,text='SHOW',command=showresulttableshow)
bt.place(x=60,y=250)

t.mainloop()