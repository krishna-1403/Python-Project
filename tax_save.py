import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

def open_link(url):
    webbrowser.open_new(url)
def taxsavescr():
    t=tkinter.Tk()
    t.geometry('800x800')
    xt=[]
    xz=[]
    def taxcal():
        x=float(h.get())
        if x<300000:
            k.insert(0,0)
            n.insert(0, x)
        elif x>300000 and x<600000:
            v=(x*5)/100
            t=(x-v)
            k.insert(0, v)
            n.insert(0, t)
        elif x>600000 and x<900000:
            v=(x*10)/100
            t=(x-v)
            k.insert(0, v)
            n.insert(0, t)
        elif x>900000 and x<1200000:
            v=(x*15)/100
            t=(x-v)
            k.insert(0, v)
            n.insert(0, t)
        elif x>1200000 and x<1500000:
            v=(x*20)/100
            t=(x-v)
            k.insert(0, v)
            n.insert(0, t)
        else:
            v=(x*30)/100
            t=(x-v)
            k.insert(0, v)
            n.insert(0, t)
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
    def cd():
        t.destroy()
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=int(f.get())
        xc=float(h.get())
        xd=float(k.get())
        xe=float(n.get())
        
        sql="insert into tax values(%d,%d,%f,%f,%f)"%(xa,xb,xc,xd,xe)
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
    e=Label(t,text='dep_id',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f=ttk.Combobox(t,width=15)
    dep()
    f['values']=xz
    f.place(x=250,y=110)
    g=Label(t,text='ctc',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=15,bg='#FDFCCD')            #entry for variable(h)
    h.place(x=250,y=150)
    j=Label(t,text='tax_computation',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=190)
    k=Entry(t,width=15,bg='#FDFCCD')            #entry for slab(k)
    k.place(x=250,y=190)
    m=Label(t,text='net_amount.',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=230)
    tax=Button(t,text='tax',command=taxcal)    #btn for close
    tax.place(x=350,y=230)
    n=Entry(t,width=15,bg='#FDFCCD')            #entry for grade(n)
    n.place(x=250,y=230)
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=350)
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=350)
    # Create a label with a hyperlink
    link_label =Label(t, text="check tax property under 2024/25", fg="blue", cursor="hand2")
    link_label.place(x=500,y=292)

    # Bind the label to the open_link function
    link_label.bind("<Button-1>", lambda e: open_link("https://cleartax.in/s/income-tax-slabs"))
    note_label=Label(t,text="Note:- Here (net_amount=(ctc-tax)+variable)Yearly",bg='#FDFCCD',font=10)
    note_label.place(x=50,y=290)
    
                     
    
    t.mainloop()