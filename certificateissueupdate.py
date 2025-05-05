import tkinter
from tkinter import * 
from tkcalendar import DateEntry
import pymysql
from tkinter import messagebox
def showcertificateissueupdate():
    t=tkinter.Tk()
    t.title('Certificate Issue')
    t.geometry('700x700')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select certificateno,courseid,dateofappear,result from certificateissue where rollno=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        messagebox.showerror('Message','Found')
        e2.insert(0,str(data[0]))
        e3.insert(0,str(data[1]))
        e4.insert(0,data[1])
        e5.insert(0,data[1])
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=e4.get()
        xf=e5.get()
        sql="update certificateissue set certificateno ='%s',courseid='%s',dateofappear ,result , where rollno=%d"%(xb,xc,xd,xf,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Updated')
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        db.close()
    z=Label(t,text='Certificate Issue',fg='navyblue',font='arial,30')       
    z.place(x=300,y=10)
    
    a=Label(t,text='Roll No.',font='arial 20',fg='red')
    a.place(x=50,y=100)
    e1=Entry(t,width=40)
    e1.place(x=300,y=100)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=550,y=100)
    
    b=Label(t,text='Certificate No.',font='arial 20',fg='red')
    b.place(x=50,y=200)
    e2=Entry(t,width=40)
    e2.place(x=300,y=200)
    
    c=Label(t,text='Course ID',font='arial 20',fg='red')
    c.place(x=50,y=300)
    e3=Entry(t,width=40)
    e3.place(x=300,y=300)
    
    a=Label(t,text='Date of Appear',font='arial 20',fg='red')
    a.place(x=50,y=400)
    e4=DateEntry(t,width=40)
    e4.place(x=300,y=400)
    
    a=Label(t,text='Result',font='arial 20',fg='red')
    a.place(x=50,y=500)
    e5=Entry(t,width=40)
    e5.place(x=300,y=500)
    
    bt=Button(t,text='Update',command=updatedata)
    bt.place(x=550,y=500)


    t.mainloop()