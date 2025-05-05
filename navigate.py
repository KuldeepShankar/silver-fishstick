import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('700x700')
t.title('Students Save')
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
i=0
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
    cur=db.cursor()
    sql="select * from students"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        x1.append(res[0])
        x2.append(res[1])
        x3.append(res[2])
        x4.append(res[3])
        x5.append(res[4])
        x6.append(res[5])
    db.close()
    
def firstdata():
    global i
    i=0
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,str(x1[i]))
    e2.insert(0,x2[i])
    e3.insert(0,x3[i])
    e4.insert(0,x4[i])
    e5.insert(0,str(x5[i]))
    e6.insert(0,x6[i])

def lastdata():
    global i
    i=len(x1)-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,str(x1[i]))
    e2.insert(0,x2[i])
    e3.insert(0,x3[i])
    e4.insert(0,x4[i])
    e5.insert(0,str(x5[i]))
    e6.insert(0,x6[i])

def nextdata():
    global i
    i=i+1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,str(x1[i]))
    e2.insert(0,x2[i])
    e3.insert(0,x3[i])
    e4.insert(0,x4[i])
    e5.insert(0,str(x5[i]))
    e6.insert(0,x6[i])


def prevdata():
    global i
    i=i-1
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)
    e5.delete(0,100)
    e6.delete(0,100)
    e1.insert(0,str(x1[i]))
    e2.insert(0,x2[i])
    e3.insert(0,x3[i])
    e4.insert(0,x4[i])
    e5.insert(0,str(x5[i]))
    e6.insert(0,x6[i])


he=Label(t,text='Student',fg='#2B2730',font='arial 30')
he.pack() 

a=Label(t, text='Roll No:')
a.place(x=50, y=120)
e1 = Entry(t, width=30)
e1.place(x=400, y=120)


b=Label(t, text='Student ID:')
b.place(x=50, y=160)
e2 = Entry(t, width=30)
e2.place(x=400, y=160)


c=Label(t, text='Name:')
c.place(x=50, y=200)
e3 = Entry(t, width=30)
e3.place(x=400, y=200)


d=Label(t, text='Address:')
d.place(x=50, y=240)
e4 = Entry(t, width=30)
e4.place(x=400, y=240)


e=Label(t, text='Phone:')
e.place(x=50, y=280)
e5 = Entry(t, width=30)
e5.place(x=400, y=280)


f=Label(t, text='Email:')
f.place(x=50, y=320)
e6 = Entry(t, width=30)
e6.place(x=400, y=320)

s=Button(t,text='First',font='comicsensms 19 italic',fg='#2B2730',command=firstdata)
s.place(x=50,y=370)

s1=Button(t,text='Next',font='comicsensms 19 italic',fg='#2B2730',command=nextdata)
s1.place(x=150,y=370)

s2=Button(t,text='Last',font='comicsensms 19 italic',fg='#2B2730',command=lastdata)
s2.place(x=250,y=370)
s3=Button(t,text='Previous',font='comicsensms 19 italic',fg='#2B2730',command=prevdata)
s3.place(x=350,y=370)
filldata()
t.mainloop()
