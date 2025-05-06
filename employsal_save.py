import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('800x800')
def cd():
    t.destroy()
def savedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='payrol')
    cur=db.cursor()
    xa=int(d.get())
    xb=int(f.get())
    xc=h.get()
    xd=(k.get())
    xe=(n.get())
    
    sql="insert into employeesalarydata values(%d,%d,'%s','%s','%s')"%(xa,xb,xc,xd,xe)
    cur.execute(sql)
    db.commit()
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    k.delete(0,100)
    n.delete(0,100)
    
    db.close()
    messagebox.showinfo("hii",'saved')

bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
bv.place(x=10,y=10)

a=Label(t,text='Employee_salary',fg='red',bg='#FDFCCD',font=('Algerian',25))
a.place(x=250,y=15)
b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
b.place(x=50,y=70)
d=Entry(t,width=25,bg='#FDFCCD')            #entry for ID(d)
d.place(x=250,y=70)
e=Label(t,text='ctc',font=('algerian',12),bg='#FDFCCD')
e.place(x=50,y=110)
f=Entry(t,width=25,bg='#FDFCCD')            #entry for ctc(f)
f.place(x=250,y=110)
g=Label(t,text='variable',font=('algerian',12),bg='#FDFCCD')
g.place(x=50,y=150)
h=Entry(t,width=25,bg='#FDFCCD')            #entry for variable(h)
h.place(x=250,y=150)
j=Label(t,text='slab',font=('algerian',12),bg='#FDFCCD')
j.place(x=50,y=190)
k=Entry(t,width=25,bg='#FDFCCD')            #entry for slab(k)
k.place(x=250,y=190)
m=Label(t,text='grade.',font=('algerian',12),bg='#FDFCCD')
m.place(x=50,y=230)
n=Entry(t,width=25,bg='#FDFCCD')            #entry for grade(n)
n.place(x=250,y=230)

btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
btn1.place(x=150,y=350)
btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
btn2.place(x=250,y=350)


t.mainloop()