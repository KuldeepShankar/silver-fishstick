import tkinter
from tkinter import *
from coursesave import *
from coursefind import *
from courseupdate import *
from coursedelete import *
from courseshow import *
t=tkinter.Tk()
t.geometry('700x700')
t.title('Courses')
t.config(bg='#005C78')

he=Label(t,text='Courses Dashboard',fg='red',bg='#021526',font='comicsensms 30 italic')
he.pack(fill='x')

f1=Frame(t,bg='#021526',borderwidth=6,relief=SUNKEN)
f1.pack(fill='both',expand=True,padx=20, pady=20)

f2 =Frame(f1,bg="#3a7ebf")
f2.pack(side="left", fill="both", expand=True, padx=(0, 10))

f3 =Frame(f1,bg="#222222")
f3.pack(side="right", fill="both", expand=True, padx=(10, 0))

bt=Button(t,text='SAVE',width=20,height=2,bg='#0A1D56',command=showcoursesave)
bt.place(x=50,y=200)

bt=Button(t,text='FIND',width=20,height=2,bg='#0A1D56',command=showcoursefind)
bt.place(x=50,y=300)

bt=Button(t,text='UPDATE',width=20,height=2,bg='#0A1D56',command=showcourseupdate)
bt.place(x=50,y=400)

bt=Button(t,text='DELETE',width=20,height=2,bg='#0A1D56',command=showcoursedelete)
bt.place(x=50,y=500)

bt=Button(t,text='SHOW',width=20,height=2,bg='#0A1D56',command=showcourseshow)
bt.place(x=50,y=600)

t.mainloop()