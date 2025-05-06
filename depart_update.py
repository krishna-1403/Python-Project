import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def depupdatescr():
    t=tkinter.Tk()
    t.geometry('800x800')
    def cd():
        t.destroy()
    
    xt=[]
    def data():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select depid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(d.get())
        if x in xt:
            sql="select depname,hod from department where depid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            f.delete(0,100)
            h.delete(0,100)
            
            f.insert(0, data[0])
            h.insert(0, data[1])
           
            db.close()
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=f.get()
        xc=h.get()
        if (xa=="") or (xb=="") or (xc==""):
            messagebox.showerror('Entry Error','something went wrong!!')
        else:
            sql="update department set depname='%s',hod='%s' where depid=%d"%(xb,xc,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hii','updated')
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            db.close()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='DEPARTMENT',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='Dept_Id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=200,y=70)
    btn2=Button(t,text='Find',font=('algerian',12),bg='red',command=finddata)     # btn for find
    btn2.place(x=170,y=110)  
    e=Label(t,text='Dep_Name',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=150)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=150)
    g=Label(t,text='HOD',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=190)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=190)
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=350,y=370)      
    btn2=Button(t,text='update',bg='Red',font=('algerian',12),command=updatedata)
    btn2.place(x=50,y=370)
        
    t.mainloop()