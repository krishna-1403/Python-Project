import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from calendar import month_name
def emplevsave():
    t=tkinter.Tk()
    t.geometry('800x800')
    def cd():
        t.destroy()
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
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=f.get()
        xc=int(h.get())
        xd=(k.get())
        if (xa=="") or (xb=="") or (xc=="") or (xd==""):
            messagebox.showerror('Entry Error','something went wrong!!')
            t.destroy()
        else:
            sql="insert into empleave values(%d,'%s',%d,'%s')"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            db.close()
            messagebox.showinfo("hii",'saved')
            t.destroy()
            
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    selected_month = tkinter.StringVar()
    
    a=Label(t,text='Employee_leave',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=250,y=70)
    e=Label(t,text='month',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f = ttk.Combobox(t, textvariable=selected_month,width=15)
    f['values'] = [month for month in month_name if month]
    f['state'] = 'readonly'  # Make the combobox read-only
    f.place(x=250,y=110)
    g=Label(t,text='No of leave',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=15,bg='#FDFCCD')            #entry for no of leave(h)
    h.place(x=250,y=150)
    j=Label(t,text='leave_type',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=190)
    k=ttk.Combobox(t,width=15)
    values=['paid','unpaid']
    k['values']=values
    k.place(x=250,y=190)
    
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=350)
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=350)
    
    
    t.mainloop()