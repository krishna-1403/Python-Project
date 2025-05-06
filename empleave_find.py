import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from calendar import month_name
def emplevfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    xt=[]
    xy=[]
    def data():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from empdata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def mahina():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select month from empleave"
        cur.execute(sql)
        data=cur.fetchall()
        for m in data:
            xy.append(m[0])
        db.close()
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(d.get())
        y=f.get()
        if x in xt and y in xy:
            sql="select noleave,type from empleave where empid=%s and month=%s"
            cur.execute(sql,(x,y))
            data=cur.fetchone()
            h.delete(0,100)
            k.delete(0,100)
            h.insert(0, data[0])
            k.insert(0, data[1])
            db.close()
        
        else:
            messagebox.showinfo('check id','Invalid Id Used')
            t.destroy()
    def cd():
        t.destroy()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    #selected_month = tkinter.StringVar()
    
    a=Label(t,text='employee_leave',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d['state'] = 'readonly'
    d.place(x=250,y=70)
    e=Label(t,text='Month',font=('algerian',12),bg='#FDFCCD')
    e.place(x=450,y=70)
    f = ttk.Combobox(t,width=15)
    mahina()
    f['values'] = xy
    f['state'] = 'readonly'  # Make the combobox read-only
    f.place(x=600,y=70)
    btn2=Button(t,text='Find',font=('algerian',12),bg='red',command=finddata)     # btn for find
    btn2.place(x=400,y=110)  
    
    g=Label(t,text='No of leave',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=190)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=190)
    j=Label(t,text='TYPE',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=230)
    k=Entry(t,width=25,bg='#FDFCCD')            #entry for email(k)
    k.place(x=250,y=230)
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=370)  
        
        
    t.mainloop()