import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
def account():
    t=tkinter.Tk()
    t.geometry('800x800')
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=(d.get())
        xb=f.get()
        xc=h.get()
        xd=k.get()
        if (xa=="") or (xb=="") or (xc=="") or (xd==""):
            messagebox.showerror('Entry Error','something went wrong!!')
        else:
            sql="insert into account values('%s','%s','%s','%s')"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            k.delete(0,100)
            
            db.close()
            messagebox.showinfo("hii",'saved')
            t.destroy()
    bv=Canvas(t,height=800,width=800,bg="#2E6A6B")
    bv.place(x=1,y=1)
    a=Label(t,text='Ragistration',font=('STENCIL','25',),bg='#2E6A6B',fg='#ffffff')
    a.place(x=300,y=50)
    bv.create_line(320,95,510,95,width='3',fill='#EF88BE' )
    bx=Canvas(t,height=600,width=600,bg="white")
    bx.place(x=100,y=120)
    b=Label(t,text='User_Name:-',font='5')
    b.place(x=160,y=140)
    d=Entry(t,width=20,bg='yellow')         #Entry for Name
    d.place(x=360,y=145)
    e=Label(t,text='Email:-',font='5')
    e.place(x=160,y=190)
    f=Entry(t,width=20,bg='yellow')         #Entry for email
    f.place(x=360,y=199)
    g=Label(t,text='Mobile_No:-',font='5')
    g.place(x=160,y=240)
    h=Entry(t,width=20,bg='yellow')         #Mobile No.
    h.place(x=360,y=245)
    j=Label(t,text='Password:-',font='5')
    j.place(x=160,y=290)
    k=Entry(t,width='20',show='*',bg='yellow')      #password
    k.place(x=360,y=295)
    m=Button(t,text='Submit',bg='pink',font='5',command=savedata)
    m.place(x=260,y=395)
    
    
    
    
    
    t.mainloop()