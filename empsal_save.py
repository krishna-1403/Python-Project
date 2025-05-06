import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from calendar import month_name
def empsalsave():
    t=tkinter.Tk()
    t.geometry('800x800')
    xt=[]
    def data():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select empid from empdata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def showvar():
      x=float(f.get())
      if x<500000:
        v=(x*2.5)/100
        h.insert(0,v)
      elif (x>500000):
        v1=(x*75)/100
        x1=(v1*2.5)/100
        v2=(x*25)/100
        x2=(v2*5)/100
        v=(x1+x2)
        h.insert(0,v)
    def showslab():
        x=float(f.get())
        if x<300000:
            k.insert(0,0)
        elif x>300000 and x<600000:
            v=(x*5)/100
            k.insert(0, v)
        elif x>600000 and x<900000:
            v=(x*10)/100
            k.insert(0, v)
        elif x>900000 and x<1200000:
            v=(x*15)/100
            k.insert(0, v)
        elif x>1200000 and x<1500000:
            v=(x*20)/100
            k.insert(0, v)
        else:
            v=(x*30)/100
            k.insert(0, v)
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=f.get()
        xc=(h.get())
        xd=(k.get())
        xe=(n.get())
        
        if (xa=="") or (xb=="") or (xc=="") or (xd=="") or (xe==""):
            messagebox.showerror('Entry Error','something went wrong!!')
            t.destroy()
        else:
            sql="insert into empsal values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            n.delete(0,100)
            db.close()
            messagebox.showinfo("hii",'saved')
            t.destroy()
    def cd():
        t.destroy()
    
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    #selected_month = tkinter.StringVar()
    a=Label(t,text='employee_salary',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=250,y=70)
    
    '''e=Label(t,text='Month',font=('algerian',12),bg='#FDFCCD')
    e.place(x=450,y=70)
    f = ttk.Combobox(t, textvariable=selected_month)
    f['values'] = [month for month in month_name if month]
    f['state'] = 'readonly'  # Make the combobox read-only
    f.place(x=600,y=70)'''
    
    e=Label(t,text='ctc',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for CTC(f)
    f.place(x=250,y=110)
    g=Label(t,text='variable',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for variables(h)
    h.place(x=250,y=150)
    btnvar=Button(t,text='show_var',command=showvar)
    btnvar.place(x=420,y=150)
    j=Label(t,text='slab',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=190)
    k=Entry(t,width=25,bg='#FDFCCD')            #entry for Slab(k)
    k.place(x=250,y=190)
    btnslb=Button(t,text='show_slab',command=showslab)
    btnslb.place(x=420,y=190)
    m=Label(t,text='grade',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=230)
    n=Entry(t,width=25,bg='#FDFCCD')            #entry for Grade(n)
    n.place(x=250,y=230)
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=370)  
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=370)
        
    t.mainloop()