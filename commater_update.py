import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def comupdatescr():
    t=tkinter.Tk()
    t.geometry('800x800')
    def cd():
        t.destroy()
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
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(d.get())
        if x in xt:
            sql="select name,address,email,phn,regno from commaster where comid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            n.delete(0,100)
            q.delete(0,100)
            f.insert(0, data[0])
            h.insert(0, data[1])
            k.insert(0, data[2])
            n.insert(0, data[3])
            q.insert(0, data[4])
        else:
            messagebox.showinfo('check id','Invalid Id Used')
            t.destroy()
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=f.get()
        xc=h.get()
        xd=k.get()
        xe=n.get()
        xf=q.get()
        if (xa=="") or (xb=="") or (xc=="") or (xd=="") or (xe=="") or (xf==""):
            messagebox.showerror('Entry Error','something went wrong!!')
        else:
            sql="update commaster set name='%s',address='%s',email='%s',phn='%s',regno='%s' where comid=%d"%(xb,xc,xd,xe,xf,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hii','updated')
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            n.delete(0,100)
            q.delete(0,100)
            db.close()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='Company',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='Company_Id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=200,y=70)
    btn2=Button(t,text='Find',font=('algerian',12),bg='red',command=finddata)     # btn for find
    btn2.place(x=170,y=110)  
    e=Label(t,text='Name',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=150)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=150)
    g=Label(t,text='Address',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=190)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=190)
    j=Label(t,text='Email',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=230)
    k=Entry(t,width=25,bg='#FDFCCD')            #entry for email(k)
    k.place(x=250,y=230)
    m=Label(t,text='Mobile_No.',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=270)
    n=Entry(t,width=25,bg='#FDFCCD')            #entry for mobile(n)
    n.place(x=250,y=270)
    p=Label(t,text='Reg_No.',font=('algerian',12),bg='#FDFCCD')
    p.place(x=50,y=310)
    q=Entry(t,width=25,bg='#FDFCCD',)           #Entry for reg(q)
    q.place(x=250,y=310)
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=350,y=370)      
    btn2=Button(t,text='update',bg='Red',font=('algerian',12),command=updatedata)
    btn2.place(x=50,y=370)
     
        
        
        
        
        
    t.mainloop()