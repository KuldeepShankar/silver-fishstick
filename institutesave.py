import tkinter
import pymysql
from tkinter import * 
from tkinter  import messagebox
def showinstitutesave():
    t=tkinter.Tk()
    t.title('Institute')
    t.geometry('1080x700')
    
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=int(e6.get())
        sql="insert into institute values('%s','%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql) 
        db.commit()
        messagebox.showinfo('Message','saved')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        
    
    z=Label(t,text='Institute',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Institute ID',font='arial,30',fg='red')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    b=Label(t,text='Institute Name',font='arial,30',fg='red')
    b.place(x=50,y=180)
    e2=Entry(t,width=40)
    e2.place(x=300,y=180)
    
    c=Label(t,text='Institutes Address',font='arial,30',fg='red')
    c.place(x=50,y=260)
    e3=Entry(t,width=40)
    e3.place(x=300,y=260)
    
    d=Label(t,text='Phone',font='arial,30',fg='red')
    d.place(x=50,y=320)
    e4=Entry(t,width=40)
    e4.place(x=300,y=320)
    
    e=Label(t,text='Email',font='arial,30',fg='red')
    e.place(x=50,y=400)
    e5=Entry(t,width=40)
    e5.place(x=300,y=400)
    
    f=Label(t,text='Registration no.',font='arial,30',fg='red')
    f.place(x=50,y=480)
    e6=Entry(t,width=40)
    e6.place(x=300,y=480)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=40,y=550)
    
    t.mainloop()