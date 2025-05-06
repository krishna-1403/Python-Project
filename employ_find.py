import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
def empfindscr():
    class PlaceholderEntry(tkinter.Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='black', *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self._clear_placeholder)
            self.bind("<FocusOut>", self._add_placeholder)

            self._add_placeholder()

        def _clear_placeholder(self, e):
            if self['fg'] == self.placeholder_color:
                self.delete(0, tkinter.END)
                self['fg'] = self.default_fg_color

        def _add_placeholder(self, e=None):
            if not self.get():
                self['fg'] = self.placeholder_color
                self.insert(0, self.placeholder)
    def show_calendar():
        '''# Create a new window for the calendar
        cal_window = tkinter.Toplevel(t)
        cal_window.title("Select a Date")

        # Create a Calendar widget
        cal = Calendar(cal_window, selectmode='day', year=2024, month=9, day=24)
        cal.pack(pady=20)
        # Function to fetch the selected date
        def fetch_date():
            selected_date = cal.get_date()
            k1.delete(0, tkinter.END)  # Clear the entry box
            k1.insert(0, selected_date)  # Insert the selected date
            cal_window.destroy()  # Close the calendar window
            
        # Add a button to fetch the selected date
        fetch_button = tkinter.Button(cal_window, text="Get Date", command=fetch_date)
        fetch_button.pack(pady=10)'''
    t=tkinter.Tk()
    t.geometry('800x800')
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
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        x=int(d.get())
        if x in xt:
            sql="select name,address,doj,phn,design,depid from empdata where empid=%d"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            f.delete(0,100)
            h.delete(0,100)
            k1.delete(0,100)
            n.delete(0,100)
            q.delete(0,100)
            s.delete(0,100)
            f.insert(0, data[0])
            h.insert(0, data[1])
            k1.insert(0, data[2])
            n.insert(0, data[3])
            q.insert(0, data[4])
            s.insert(0, data[5])
            db.close()
        else:
            messagebox.showerror('check id','Invalid Id Used')
    def cd():
        t.destroy()
    #Canvas
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    a=Label(t,text='Employee',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)    
    b=Label(t,text='emp_Id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=ttk.Combobox(t,width=15)
    data()
    d['values']=xt
    d.place(x=200,y=70)
    btn2=Button(t,text='Find',font=('algerian',12),bg='red',command=finddata)     # btn for find
    btn2.place(x=170,y=110)  
    e=Label(t,text='emp_name',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=150)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=150)
    g=Label(t,text='Address',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=190)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=190)
    j=Label(t,text='doj',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=230)
    k1=PlaceholderEntry(t,width=25,bg='#FDFCCD',placeholder='MM/DD/YY')            #entry for doj(k)
    k1.place(x=250,y=230)
    m=Label(t,text='Mobile_No.',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=270)
    n=Entry(t,width=25,bg='#FDFCCD')            #entry for mobile(n)
    n.place(x=250,y=270)
    p=Label(t,text='designation.',font=('algerian',12),bg='#FDFCCD')
    p.place(x=50,y=310)
    q=Entry(t,width=25,bg='#FDFCCD',)           #Entry for reg(q)
    q.place(x=250,y=310)
    r=Label(t,text='Dep_Id',font=('algerian',12),bg='#FDFCCD')
    r.place(x=50,y=350)
    s=ttk.Combobox(t,width=15)
    dep()
    s['values']=xz
    s.place(x=250,y=350)
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=400)  
        
        
    t.mainloop()