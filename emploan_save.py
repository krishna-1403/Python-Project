import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
def emploansave():
    t=tkinter.Tk()
    t.geometry('800x800')
    def cd():
        t.destroy()
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=int(f.get())
        xc=float(h.get())
       
        sql="insert into emploan values(%d,%d,%f)"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        
        db.close()
        messagebox.showinfo("hii",'saved')
    
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='emp_loan',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=Entry(t,width=25,bg='#FDFCCD')            #entry for ID(d)
    d.place(x=250,y=70)
    e=Label(t,text='dep_id',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=110)
    g=Label(t,text='Loan_amount',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=150)
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=200)
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=200)
    t.mainloop()