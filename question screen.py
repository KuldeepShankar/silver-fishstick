import tkinter
import pymysql
from tkinter import * 
from tkinter  import messagebox

t=tkinter.Tk()
t.title('python')
t.geometry('700x700')
q=[]
a1=[]
a2=[]
a3=[]
a4=[]
i=0
def questionfiill():
    db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
    cur=db.cursor()
    sql="select q_name,option_a,option_b,option_c,option_d from java"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        q.append(res[0])
        a1.append(res[1])
        a2.append(res[2])
        a3.append(res[3])
        a4.append(res[4])
    db.close()
def first():
   global i
   i=0
   b.config(text=q[i])
   r1.config(text=a1[i])
   r2.config(text=a2[i])
   r3.config(text=a3[i])
   r4.config(text=a4[i])
def nextd():
    global i
    i=i+1
    b.config(text=q[i])
    r1.config(text=a1[i])
    r2.config(text=a2[i])
    r3.config(text=a3[i])
    r4.config(text=a4[i])
z=Label(t,text='Java')       
z.place(x=300,y=10)

x=IntVar()

b=Label(t,text='Question name')
b.place(x=50,y=180)

r1=Radiobutton(t,text='option_a',variable=x,value=0)
r1.place(x=50,y=220)
r2=Radiobutton(t,text='option_b',variable=x,value=1)
r2.place(x=50,y=260)
r3=Radiobutton(t,text='option_c',variable=x,value=2)
r3.place(x=50,y=300)
r4=Radiobutton(t,text='option_d',variable=x,value=3)
r4.place(x=50,y=340)

bt=Button(t,text='Next',command=nextd)
bt.place(x=40,y=520)
questionfiill()
first()
t.mainloop()