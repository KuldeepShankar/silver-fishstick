import tkinter 
from tkinter import *
import pymysql
t=tkinter.Tk()
t.geometry("700x700")
t.title('admintable')
t.Max('700x700')
t.config(bg='#2B3499')
a=Label(t,text='Admin ID',font="comicsensms 19 bold",fg='#001B79')
a.place(x=200,y=200)
e1=Entry(t,width=40)
e1.place(x=200,y=250)




t.mainloop()
