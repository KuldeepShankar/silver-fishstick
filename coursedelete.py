import tkinter
from tkinter import * 
import pymysql
from tkinter import messagebox
def showcoursedelete():
    t=tkinter.Tk()
    t.title('Courses')
    t.geometry('700x700')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        sql="select cname,durationindays from courses where courseid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        messagebox.showerror('Message','Found')
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=e1.get()
        sql="delete from courses where courseid='%s'"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Deleted')
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
    
    z=Label(t,text=' Course ',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Course ID',font='arial,30',fg='red')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=550,y=100)
    
    b=Label(t,text='Course Name',font='arial,30',fg='red')
    b.place(x=50,y=180)
    e2=Entry(t,width=40)
    e2.place(x=300,y=180)
    
    c=Label(t,text='Course duration',font='arial,30',fg='red')
    c.place(x=50,y=260)
    e3=Entry(t,width=40)
    e3.place(x=300,y=260)
    
    bt=Button(t,text='delete',command=deletedata)
    bt.place(x=550,y=260)
    t.mainloop()