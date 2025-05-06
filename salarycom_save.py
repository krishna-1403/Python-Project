import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def salsavescr():
    t=tkinter.Tk()
    t.geometry('800x800')
    xt=[]
    xz=[]
    xy=[]
    def cd():
        t.destroy()
    
    def mahina():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select month from empleave"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xy.append(res[0])
        db.close()
    def netsal():
        try:
            month = h.get()
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            
            # Execute the first query
            sql = "SELECT netamt FROM tax"
            cur.execute(sql)
            tax_data = cur.fetchall()
            
            # Execute the second query with a month filter
            sql1 = "SELECT noleave, type FROM empleave WHERE month= %s"
            cur.execute(sql1, (month,))
            leave_data = cur.fetchall()
            
            for tax_res, leave_res in zip(tax_data, leave_data):
                nt = tax_res[0]
                noleave = leave_res[0]
                leave_type = leave_res[1]
                
                print(f"Net Amount: {nt}, No. of Leaves: {noleave}, Leave Type: {leave_type}")
                
                if leave_type == 'paid':
                    np = nt / 12
                else:
                    nq = nt / 12
                    ns = ((nq / 30) * noleave)
                    np = nq - ns
                
                print(f"Calculated Net Pay: {np}")
                
                k.delete(0, 100)
                k.insert(0, np)
            
            cur.close()
            db.close()
        except Exception as e:
            print(f"An error occurred: {e}")

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
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=int(f.get())
        xc=(h.get())
        xd=float(k.get())
        
        
        sql="insert into salcomp values(%d,%d,'%s',%f)"%(xa,xb,xc,xd)
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
    
    a=Label(t,text='salary_computation',fg='red',bg='#FDFCCD',font=('Algerian',25))
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
    
    g=Label(t,text='month',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h = ttk.Combobox(t,width=15)
    mahina()
    h['values'] = xy
    h['state'] = 'readonly'  # Make the combobox read-only
    h.place(x=250,y=150)
    
    j=Label(t,text='net_payable',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=190)
    k=Entry(t,width=15,bg='#FDFCCD')            #entry for netpay(k)
    k.place(x=250,y=190)
    tax=Button(t,text='Amount',command=netsal)    #btn for close
    tax.place(x=350,y=190)
    
    
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=350)
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=350)
    
    
    t.mainloop()