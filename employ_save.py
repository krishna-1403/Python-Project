import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk
def empdatascr():
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
        # Create a new window for the calendar
        cal_window = tkinter.Toplevel(t)
        cal_window.title("Select a Date")

        # Create a Calendar widget
        cal = Calendar(cal_window, selectmode='day', month=9, day=24, year=2024)
        cal.pack(pady=20)
        # Function to fetch the selected date
        def fetch_date():
            selected_date = cal.get_date()
            formatted_date = datetime.strptime(selected_date, '%m/%d/%y').strftime('%m/%d/%y')
            k1.delete(0, END)  # Clear the entry box
            k1.insert(0, formatted_date)  # Insert the formatted date
            cal_window.destroy()
                
        # Add a button to fetch the selected date
        fetch_button = tkinter.Button(cal_window, text="Get Date", command=fetch_date)
        fetch_button.pack(pady=10)

    t=tkinter.Tk()
    t.geometry('800x800')
    #xt=[]
    xz=[]
    def cd():
        t.destroy()
    def dep():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        sql="select depid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xz.append(res[0])
        db.close()
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='eps')
        cur=db.cursor()
        xa=int(d.get())
        xb=f.get()
        xc=h.get()
        xd=(k1.get())
        xe=(n.get())
        xf=(q.get())
        xg=int(s.get())
        if (xa=="") or (xb=="") or (xc=="") or (xd=="") or (xe=="") or (xf=="") or (xg==""):
            messagebox.showerror('Entry Error','something went wrong!!')
            t.destroy()
        else:
            sql="insert into empdata values(%d,'%s','%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf,xg)
            cur.execute(sql)
            db.commit()
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            k1.delete(0,100)
            n.delete(0,100)
            q.delete(0,100)
            s.delete(0,100)
            db.close()
            messagebox.showinfo("hii",'saved')
            t.destroy()
    bv=Canvas(t,height=800,width=800,bg="#FDFCCD")
    bv.place(x=10,y=10)
    
    #image = Image.open("C:\payroll\cal1.jpg")
    #symbol_image = ImageTk.PhotoImage(image)
    
    a=Label(t,text='Employee',fg='red',bg='#FDFCCD',font=('Algerian',25))
    a.place(x=250,y=15)
    b=Label(t,text='emp_id',font=('algerian',12),bg='#FDFCCD')
    b.place(x=50,y=70)
    d=Entry(t,width=25,bg='#FDFCCD')            #entry for ID(d)
    d.place(x=250,y=70)
    e=Label(t,text='emp_name',font=('algerian',12),bg='#FDFCCD')
    e.place(x=50,y=110)
    f=Entry(t,width=25,bg='#FDFCCD')            #entry for name(f)
    f.place(x=250,y=110)
    g=Label(t,text='Address',font=('algerian',12),bg='#FDFCCD')
    g.place(x=50,y=150)
    h=Entry(t,width=25,bg='#FDFCCD')            #entry for address(h)
    h.place(x=250,y=150)
    j=Label(t,text='doj',font=('algerian',12),bg='#FDFCCD')
    j.place(x=50,y=190)
    k1=PlaceholderEntry(t,width=25,bg='#FDFCCD',placeholder='MM/DD/YY')            #entry for doj(k1)
    k1.place(x=250,y=190)
    k = Button(t,text="Add Date", command=show_calendar)
    k.place(x=400,y=190)
    m=Label(t,text='Mobile_No.',font=('algerian',12),bg='#FDFCCD')
    m.place(x=50,y=230)
    n=Entry(t,width=25,bg='#FDFCCD')            #entry for mobile(n)
    n.place(x=250,y=230)
    p=Label(t,text='designation',font=('algerian',12),bg='#FDFCCD')
    p.place(x=50,y=270)
    q=Entry(t,width=25,bg='#FDFCCD',)           #Entry for designation(q)
    q.place(x=250,y=270)
    r=Label(t,text='Dep_Id',font=('algerian',12),bg='#FDFCCD')
    r.place(x=50,y=310)
    s=ttk.Combobox(t,width=15)
    dep()
    s['values']=xz
    s['state'] = 'readonly'
    s.place(x=250,y=310)
    btn1=Button(t,text='Close',font=('algerian',12),bg='red',command=cd)    #btn for close
    btn1.place(x=150,y=390)
    btn2=Button(t,text='Save',font=('algerian',12),bg='red',command=savedata)     # btn for save
    btn2.place(x=250,y=390)
    

    t.mainloop()
