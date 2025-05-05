import tkinter
import pymysql
from tkinter import * 
from tkinter  import messagebox
def showresulttabledelete():
    t=tkinter.Tk()
    t.title('Result table')
    t.geometry('700x700')
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select courseid,name,totalscore from resulttable where rollno=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        messagebox.showerror('Message','Found')
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=int(e1.get())    
        sql="delete from resulttable where rollno=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Deleted')
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
    z=Label(t,text='Result table',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Roll no.',font='arial,30',fg='#3D365C')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=550,y=100)
    
    b=Label(t,text='Course ID',font='arial,30',fg='#3D365C')
    b.place(x=50,y=180)
    e2=Entry(t,width=40)
    e2.place(x=300,y=180)
    
    c=Label(t,text='Name',font='arial,30',fg='#3D365C')
    c.place(x=50,y=260)
    e3=Entry(t,width=40)
    e3.place(x=300,y=260)
    
    d=Label(t,text='Total score',font='arial,30',fg='#3D365C')
    d.place(x=50,y=320)
    e4=Entry(t,width=40)
    e4.place(x=300,y=320)
    
        
        
    bt=Button(t,text='Delete',command=deletedata)
    bt.place(x=550,y=320)
    
    t.mainloop()