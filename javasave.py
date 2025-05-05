import tkinter
import pymysql
from tkinter import * 
from tkinter  import messagebox
def showjavasave():
    t=tkinter.Tk()
    t.title('python')
    t.geometry('700x700')
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        xg=e7.get()
        sql="insert into java values('%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql) 
        db.commit()
        messagebox.showinfo('Message','saved')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
    
    z=Label(t,text='Java',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Question ID',font='arial,30',fg='#3D365C')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    b=Label(t,text='Question Name',font='arial,30',fg='#3D365C')
    b.place(x=50,y=180)
    e2=Entry(t,width=40)
    e2.place(x=300,y=180)
    
    c=Label(t,text='Option A',font='arial,30',fg='#3D365C')
    c.place(x=50,y=260)
    e3=Entry(t,width=40)
    e3.place(x=300,y=260)
    
    d=Label(t,text='Option B',font='arial,30',fg='#3D365C')
    d.place(x=50,y=320)
    e4=Entry(t,width=40)
    e4.place(x=300,y=320)
    
    e=Label(t,text='Option C',font='arial,30',fg='#3D365C')
    e.place(x=50,y=400)
    e5=Entry(t,width=40)
    e5.place(x=300,y=400)
    
    f=Label(t,text='Option D',font='arial,30',fg='#3D365C')
    f.place(x=50,y=480)
    e6=Entry(t,width=40)
    e6.place(x=300,y=480)
    
    g=Label(t,text="Correct answer.... ",font='arial,30',fg='#3D365C')
    g.place(x=50,y=560)
    e7=Entry(t,width=40)
    e7.place(x=300,y=560)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=40,y=620)
    
    t.mainloop()