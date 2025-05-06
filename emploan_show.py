import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
st=''
def emploanshow():
    t=tkinter.Tk()
    t.geometry('800x800')
    global st
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid,depid,loan from emploan"
        cur.execute(sql)
        data=cur.fetchall()
        global st
        for res in data:
            st=st+'\n '+str(res[0])+'\t'+str(res[1])+'\t'+str(res[2])
        b.insert(END, st)
    b=Text(t,width=100,height=100)
    b.place(x=200,y=20)
    filldata()
    
    
    t.mainloop()
