import tkinter as tk
import pymysql
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import ImageTk,Image
import random
import Ragister
from Ragister import *
import dashbod
from dashbod import *

def login():
    xa = b1.get()
    xb = d1.get()
    if (xa == "") or (xb == ""):
        messagebox.showerror('Entry Error', 'Type Username and Password!!')
    else:
        t.config(cursor="watch")
        btn1.config(text="Loading...", state=tk.DISABLED)
        t.update_idletasks()
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            print('Connected Successfully.')
        except Exception as e:
            messagebox.showerror('Connection', f'Connection not established: {e}')
            btn1.config(text="Login", state=tk.NORMAL)
            t.config(cursor="")
            return
        try:
            sql = "use eps"
            cur.execute(sql)
            sql = "select * from account where uname = %s and password = %s"
            cur.execute(sql, (xa, xb))
            data = cur.fetchone()
            if data is None:
                messagebox.showinfo('Invalid', 'Invalid username and password!!')
                btn1.config(text="Login", state=tk.NORMAL)
                t.config(cursor="")
            else:
                messagebox.showinfo('Login', 'Login Successfully..')
                t.destroy()
                main_dashboard()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
            btn1.config(text="Login", state=tk.NORMAL)
            t.config(cursor="")
        finally:
            db.close()

def main_dashboard(): 
    root = tk.Tk() 
    app = PayrollSystem(root) 
    root.mainloop()

def forgot_password():
    def send_code():
        email = email_entry.get()
        if email == "":
            messagebox.showerror('Entry Error', 'Please enter your email address!')
            return
        
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
            cur = db.cursor()
            sql = "select * from account where email = %s"
            cur.execute(sql, (email,))
            data = cur.fetchone()
            if data is None:
                messagebox.showinfo('Invalid', 'Email address not found!')
            else:
                global verification_code
                verification_code = str(random.randint(100000, 999999))
                
                sender_email = "agrawalkrishna3846@gmail.com"
                sender_password = "krishna@1403"
                receiver_email = email
                subject = "Password Reset Verification Code"
                body = f"Your password reset verification code is {verification_code}"

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                try:
                    server = smtplib.SMTP('smtp.example.com', 534)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, receiver_email, text)
                    server.quit()
                    messagebox.showinfo('Success', 'Verification code sent! Check your email.')

                    # Open the code verification window
                    verify_code_window(email)
                except Exception as e:
                    messagebox.showerror('Error', f'Failed to send email: {e}')
            db.close()
        except Exception as e:
            messagebox.showerror('Connection', f'Connection not established: {e}')

    def verify_code_window(email):
        vc_window = tk.Toplevel(t)
        vc_window.title("Verify Code")
        vc_window.geometry('300x200')

        def verify_code():
            entered_code = code_entry.get()
            if entered_code == verification_code:
                vc_window.destroy()
                new_password_window(email)
            else:
                messagebox.showerror('Invalid', 'Incorrect verification code!')

        tk.Label(vc_window, text="Enter the verification code sent to your email", bg='lightgray', fg='white').pack(pady=10)
        code_entry = tk.Entry(vc_window, width=30)
        code_entry.pack(pady=5)
        tk.Button(vc_window, text="Verify Code", bg='#832DFF', fg='white', command=verify_code).pack(pady=20)

    def new_password_window(email):
        np_window = tk.Toplevel(t)
        np_window.title("New Password")
        np_window.geometry('300x200')

        def reset_password():
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()
            if new_password == "" or confirm_password == "":
                messagebox.showerror('Entry Error', 'Please fill out all fields!')
                return
            if new_password != confirm_password:
                messagebox.showerror('Mismatch', 'Passwords do not match!')
                return
            
            try:
                db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
                cur = db.cursor()
                sql = "update account set password = %s where email = %s"
                cur.execute(sql, (new_password, email))
                db.commit()
                messagebox.showinfo('Success', 'Password reset successfully!')
                np_window.destroy()
                db.close()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to reset password: {e}')

        tk.Label(np_window, text="Enter your new password", bg='lightgray', fg='white').pack(pady=10)
        new_password_entry = tk.Entry(np_window, width=30, show='*')
        new_password_entry.pack(pady=5)
        tk.Label(np_window, text="Confirm your new password", bg='lightgray', fg='white').pack(pady=10)
        confirm_password_entry = tk.Entry(np_window, width=30, show='*')
        confirm_password_entry.pack(pady=5)
        tk.Button(np_window, text="Reset Password", bg='#832DFF', fg='white', command=reset_password).pack(pady=20)

    fp_window = tk.Toplevel(t)
    fp_window.title("Forgot Password")
    fp_window.geometry('300x200')

    tk.Label(fp_window, text="Enter your registered email", bg='lightgray', fg='white').pack(pady=10)
    email_entry = tk.Entry(fp_window, width=30)
    email_entry.pack(pady=5)
    tk.Button(fp_window, text="Send Code", bg='#832DFF', fg='white', command=send_code).pack(pady=20)

t = tk.Tk()
t.geometry('1024x1024')
t.title("LOGIN PAGE")
t.resizable(False,False)
image=Image.open("payroll1.png")
photo=ImageTk.PhotoImage(image)
l2=Label(image=photo,width=1024,height=1024)
l2.pack(fill=X)
t.configure(bg="pink")

# Add Payroll Management System label
frame = tk.Frame(t, bg="yellow")
frame.place(x=210,y=250)

a1=tk.Label(frame,text='''Payroll Management System ''',font='Arial 18 bold',bg='yellow',fg='#000')
a1.grid(row=0,column=1,padx=10,pady=10)

a = tk.Label(frame, text='-Username', bg='yellow', fg='black')
a.grid(row=1, column=1, padx=10, pady=10, sticky="e")
b1 = tk.Entry(frame, width=20, bg='white', fg='black')
b1.grid(row=1, column=1, padx=10, pady=10)

d = tk.Label(frame, text='-Password', bg='yellow', fg='black')
d.grid(row=2, column=1, padx=10, pady=10, sticky="e")
d1 = tk.Entry(frame, width=20, bg='white', fg='black', show='*')
d1.grid(row=2, column=1, padx=10, pady=10)

btn1 = tk.Button(frame, text='Login', bg='#000', fg='white', command=login)
btn1.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

btn2 = tk.Button(frame, text='Create an account', bg='#000', fg='white', command=account)
btn2.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

forgot_pwd = tk.Label(frame, text='Forgot Password?', bg='yellow', fg='#000', cursor="hand2")
forgot_pwd.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
forgot_pwd.bind("<Button-1>", lambda e: forgot_password())

t.bind('<Return>', lambda event: login())

t.mainloop()
