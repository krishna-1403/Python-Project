import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
def depcheckscr():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('check data ')
    x=Canvas(t,height=800,width=800,bg='lightseagreen')
    x.place(x=1,y=1)
    
    xa=[]
    xb=[]
    xc=[]
    
    i=0
    def cd():
        t.destroy()
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select depid,depname,hod from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            
        db.close()
    def firstrecord():
        global i
        i=0
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        
        d.insert(0,str(xa[i]))
        f.insert(0,xb[i])
        h.insert(0,xc[i])
        
    def nextrecord():
        global i
        i=i+1
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
       
        d.insert(0,str(xa[i]))
        f.insert(0,xb[i])
        h.insert(0,xc[i])
       
    def prevrecord():
        global i
        i=i-1
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        
        d.insert(0,str(xa[i]))
        f.insert(0,xb[i])
        h.insert(0,xc[i])
        
    def lastrecord():
        global i
        i=len(xa)-1
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
       
        d.insert(0,str(xa[i]))
        f.insert(0,xb[i])
        h.insert(0,xc[i])
        
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='DEPARTMENT',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)
    b=Label(t,text='Dep_Id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=Entry(t,width=25,bg='#FDFCCD')            #entry for ID(d)
    d.place(x=250,y=70)
    e=Label(t,text='Dname',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=110)
    g=Label(t,text='HOD',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=150)
    
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=350)
    btn2=Button(t,text='first',font=('algerian',12),bg='red',command=firstrecord)     # btn for save
    btn2.place(x=250,y=350)
    btn3=Button(t,text='next',font=('algerian',12),bg='red',command=nextrecord)     # btn for save
    btn3.place(x=350,y=350)
    btn4=Button(t,text='previous',font=('algerian',12),bg='red',command=prevrecord)     # btn for save
    btn4.place(x=450,y=350)
    btn5=Button(t,text='last',font=('algerian',12),bg='red',command=lastrecord)     # btn for save
    btn5.place(x=550,y=350)
    filldata()
    t.mainloop()