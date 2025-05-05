import tkinter
from tkinter import * 
from tkinter import messagebox
import pymysql
def showquizappearshow():
    t=tkinter.Tk()
    t.title('Quizappear')
    t.geometry('700x700')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='quizportal')
        cur=db.cursor()
        sql="select * from quizappear"
        cur.execute(sql)
        msg=""
        data=cur.fetchall()
        for res in data:
            msg=msg+str(res[0])+"\t"
            msg=msg+str(res[1])+"\t"
            msg=msg+str(res[2])+"\t"
            msg=msg+str(res[3])+"\t"
            msg=msg+"\n"
        e.insert(END,msg)
        db.close()
            
    
    e=Text(t,width=100,height=50)
    e.place(x=50,y=20)
    filldata()
    
    t.config(bg='skyblue')
    
    t.mainloop()