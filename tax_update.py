import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def taxupdatescr():
    t=tkinter.Tk()
    t.geometry('800x800')
    def cd():
        t.destroy()
    xt=[]
    xz=[]
    def dep():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select depid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xz.append(res[0])
        db.close()
    def data():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from empdata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def taxcal():
        x=float(h.get())
        if x<300000:
            k.delete(0,100)
            k.insert(0,0)
            n.delete(0,100)
            n.insert(0, x)
            
        elif x>300000 and x<600000:
            v=(x*5)/100
            t=(x-v)
            k.delete(0,100)
            k.insert(0, v)
            n.delete(0,100)
            n.insert(0, t)
        elif x>600000 and x<900000:
            v=(x*10)/100
            t=(x-v)
            k.delete(0,100)
            k.insert(0, v)
            n.delete(0,100)
            n.insert(0, t)
        elif x>900000 and x<1200000:
            v=(x*15)/100
            t=(x-v)
            k.delete(0,100)
            k.insert(0, v)
            n.delete(0,100)
            n.insert(0, t)
        elif x>1200000 and x<1500000:
            v=(x*20)/100
            t=(x-v)
            k.delete(0,100)
            k.insert(0, v)
            n.delete(0,100)
            n.insert(0, t)
        else:
            v=(x*30)/100
            t=(x-v)
            k.delete(0,100)
            k.insert(0, v)
            n.delete(0,100)
            n.insert(0, t)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(d.get())
        if x in xt:
            sql="select depid,ctc,tax,netamt from tax where empid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            n.delete(0,100)
            
            f.insert(0, data[0])
            h.insert(0, data[1])
            k.insert(0, data[2])
            n.insert(0, data[3])
           
            db.close()
        else:
             messagebox.showinfo('check id','Invalid Id Used')
             t.destroy()
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=(d.get())
        xb=(f.get())
        xc=float(h.get())
        xd=float(k.get())
        xe=float(n.get())
        
        sql="update tax set depid=%s,ctc=%s,tax=%s,netamt=%s where empid=%s"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hii','updated')
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        k.delete(0,100)
        n.delete(0,100)
        t.destroy()
        db.close()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='tax_computation',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=250,y=70)
    btn2=Button(t,text='Find',font=('algerian',12),bg='red',command=finddata)     # btn for find
    btn2.place(x=170,y=110)  
    e=Label(t,text='dept_id',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=150)
    f=ttk.Combobox(t,width=15)
    dep()
    f['values']=xz
    f.place(x=250,y=150)
    g=Label(t,text='ctc',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=190)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for ctc(h)
    h.place(x=250,y=190)
    j=Label(t,text='tax_comp.',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=230)
    k=Entry(t,width=15,bg='#FDFCCD')            #entry for taxcomp.(k)
    k.place(x=250,y=230)
    m=Label(t,text='net_amt.',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=270)
    tax=Button(t,text='tax',command=taxcal)    #btn for close
    tax.place(x=350,y=270)
    n=Entry(t,width=15,bg='#FDFCCD')            #entry for netamt(n)
    n.place(x=250,y=270)
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=350,y=370)      
    btn2=Button(t,text='update',bg='Red',font=('algerian',12),command=updatedata)
    btn2.place(x=50,y=370)
        
        
        
        
        
        
    t.mainloop()