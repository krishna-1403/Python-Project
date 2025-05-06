import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
def comdelscr():
    t=tkinter.Tk()
    t.geometry('800x800')
    xt=[]
    def data():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select comid from commaster"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(b.get())
        sql="delete from commaster where comid=%d"%(x)
        cur.execute(sql)
        b.delete(0,100)
        messagebox.showinfo("hii",'delete')
        db.commit()
        db.close()
        t.destroy()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='Company',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15) 
    a=Label(t,text='Company_Id',bg='#FDFCCD',font=('algerian',12))
    a.place(x=50,y=70)
    b=ttk.Combobox(t,width=15)
    data()
    b['values']=xt
    b.place(x=200,y=70)
    btn1=Button(t,text='Delete',bg='#FDFCCD',font=('algerian',12),command=deletedata)
    btn1.place(x=150,y=110)
    
       
    t.mainloop()