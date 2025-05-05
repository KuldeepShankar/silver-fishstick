import tkinter
import pymysql
from tkinter import * 
from tkinter  import messagebox
def showpythondelete():
    t=tkinter.Tk()
    t.title('python')
    t.geometry('700x700')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        sql="select qname,opt1,opt2,opt3,opt4,correct from python where Qid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        messagebox.showinfo('Message','Found')
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        db.close()
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        sql="delete from python where Qid='%s'"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Deleted')
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
    z=Label(t,text='Python',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Question ID',font='arial,30',fg='red')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=600,y=100)
    
    
    b=Label(t,text='Question Name',font='arial,30',fg='red')
    b.place(x=50,y=180)
    e2=Entry(t,width=40)
    e2.place(x=300,y=180)
    
    c=Label(t,text='Option A',font='arial,30',fg='red')
    c.place(x=50,y=260)
    e3=Entry(t,width=40)
    e3.place(x=300,y=260)
    
    d=Label(t,text='Option B',font='arial,30',fg='red')
    d.place(x=50,y=320)
    e4=Entry(t,width=40)
    e4.place(x=300,y=320)
    
    e=Label(t,text='Option C',font='arial,30',fg='red')
    e.place(x=50,y=400)
    e5=Entry(t,width=40)
    e5.place(x=300,y=400)
    
    f=Label(t,text='Option D',font='arial,30',fg='red')
    f.place(x=50,y=480)
    e6=Entry(t,width=40)
    e6.place(x=300,y=480)
    
    g=Label(t,text='Correct Answer...',font='arial,30',fg='red')
    g.place(x=50,y=540)
    e7=Entry(t,width=40)
    e7.place(x=300,y=540)
    
    bt=Button(t,text='Delete',command=deletedata)
    bt.place(x=600,y=540)
    
    t.mainloop()