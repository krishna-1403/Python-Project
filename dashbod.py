import tkinter as tk
from tkinter import * 
from commaster_save import *
from commaster_find import * 
from commater_update import *
from commaster_delete import * 
from commaster_show import * 
from commaster_check import * 
from depart_save import * 
from depart_find import * 
from depart_update import * 
from depart_delete import * 
from depart_show import * 
from depart_check import * 
from employ_save import * 
from employ_find import * 
from employ_update import * 
from employ_delete import * 
from employ_show import * 
from employ_check import * 
from empsal_save import * 
from empsal_find import * 
from empsal_update import * 
#from empsal_delete import * 
from empsal_show import * 
from empsal_check import * 
from empleave_save import * 
from empleave_find import * 
from empleave_update import * 
#from empleave_delete import * 
from empleave_show import * 
from empleave_check import * 
from emploan_save import * 
from emploan_find import * 
from emploan_update import * 
from emploan_delete import * 
from emploan_show import * 
from emploan_check import * 
from tax_save import * 
from tax_find import * 
from tax_update import * 
from tax_delete import * 
from tax_show import * 
from tax_check import * 
from salarycom_save import * 
from salarycom_find import * 
from salarycom_update import * 
from salarycom_delete import * 
from salarycom_show import * 
from salarycomp_check import * 
from tkinter import messagebox
from PIL import Image,ImageTk

class PayrollSystem:
    def __init__(self, root): 
        self.root = root 
        self.root.geometry('1000x700') 
        self.root.configure(bg="#58135E") 
        # Variables to track visibility 
        self.dep_visible = False 
        self.com_visible = False 
        self.emp_visible = False 
        self.emp_sal_visible = False 
        self.emp_leave_visible = False 
        self.tax_visible = False 
        self.salary_visible = False 
        
        self.initUI()
    def initUI(self): 
        # Use grid geometry manager for better responsiveness 
        main_frame = tk.Frame(self.root, bg="#58135E") 
        main_frame.place(relx=0, rely=0, relwidth=1, relheight=1) 
        
        self.create_dashboard(main_frame) 
        self.create_buttons(main_frame) 
        
    def create_dashboard(self, frame): 
        tk.Label(frame, text='PAYROLL SYSTEM', font=('script MT bold', 25), bg='#EB3324', fg='#000000').place(x=320, y=45) 
        # Create a canvas to draw the line 
        line_canvas = tk.Canvas(frame, width=600, height=2, bg='#58135E', highlightthickness=0) 
        line_canvas.place(x=200, y=90) 
        # Draw the line 
        line_canvas.create_line(120, 1, 425, 1, fill='white') 
        tk.Label(frame, text='DASHBOARD', font=('Yu Gothic UI Semibold', 15), fg='#ffffff', bg='#377E47').place(x=400, y=130)
        
        
    def create_buttons(self, frame): 
        tk.Button(frame, text='COMPANY DATA', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_com).place(x=110, y=190) 
        tk.Button(frame, text='DEPARTMENT', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_dep).place(x=110, y=235) 
        tk.Button(frame, text='EMPLOYEE DATA', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_emp).place(x=110, y=280) 
        tk.Button(frame, text='EMPLOYEE SALARY', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_emp_sal).place(x=110, y=325) 
        tk.Button(frame, text='EMPLOYEE LEAVE', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_emp_leave).place(x=110, y=370) 
        tk.Button(frame, text='TAX COMPUTE', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_tax).place(x=110, y=415) 
        tk.Button(frame, text='SALARY COMPUTE', width=15, font=('Yu Gothic UI Semibold', 15), bg='#000000', fg='#FFFFFF', command=self.toggle_salary).place(x=110, y=460)

    def toggle_com(self): 
        if self.com_visible: 
            self.hide_com_buttons() 
        else: 
            self.show_com_buttons() 
        self.com_visible = not self.com_visible
        
    def toggle_dep(self):
        if self.dep_visible:
            self.hide_dep_buttons()
        else:
            self.show_dep_buttons()
        self.dep_visible = not self.dep_visible
        
    def toggle_emp(self): 
        if self.emp_visible: 
            self.hide_emp_buttons() 
        else: 
            self.show_emp_buttons() 
        self.emp_visible = not self.emp_visible
    
    def toggle_emp_sal(self): 
        if self.emp_sal_visible: 
            self.hide_emp_sal_buttons() 
        else: 
            self.show_emp_sal_buttons() 
        self.emp_sal_visible = not self.emp_sal_visible
        
    def toggle_emp_leave(self): 
        if self.emp_leave_visible: 
            self.hide_emp_leave_buttons() 
        else: 
            self.show_emp_leave_buttons() 
        self.emp_leave_visible = not self.emp_leave_visible 
        
    def toggle_tax(self): 
        if self.tax_visible: 
            self.hide_tax_buttons() 
        else: 
            self.show_tax_buttons() 
        self.tax_visible = not self.tax_visible
    
    def toggle_salary(self): 
        if self.salary_visible: 
            self.hide_salary_buttons() 
        else: 
            self.show_salary_buttons() 
        self.salary_visible = not self.salary_visible
        
    def show_com_buttons(self): 
        self.b1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#ffffff',command=comsavescr) 
        self.b1.place(x=350,y=190) 
        self.b2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=comfindscr) 
        self.b2.place(x=410,y=190) 
        self.b3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#ffe6e6',fg='#000000',command=comupdatescr) 
        self.b3.place(x=470,y=190) 
        self.b4=Button(self.root,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=comdelscr) 
        self.b4.place(x=550,y=190) 
        self.b5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=comshowscr) 
        self.b5.place(x=620,y=190) 
        self.b6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=comcheckscr) 
        self.b6.place(x=690,y=190)
    def hide_com_buttons(self):
        self.b1.place_forget()
        self.b2.place_forget()
        self.b3.place_forget()
        self.b4.place_forget()
        self.b5.place_forget()
        self.b6.place_forget()
        
    def show_dep_buttons(self):
        self.dep_save_btn = tk.Button(self.root, text='SAVE', font=('Yu Gothic UI Semibold', 12), bg='#99FF66', fg='#000000', command=depsavescr)
        self.dep_save_btn.place(x=350, y=235)
        self.dep_find_btn = tk.Button(self.root, text='FIND', font=('Yu Gothic UI Semibold', 12), bg='#BA281D', fg='#fff', command=depfindscr)
        self.dep_find_btn.place(x=410, y=235)
        self.dep_update_btn = tk.Button(self.root, text='UPDATE', font=('Yu Gothic UI Semibold', 12), bg='#73FBFD', fg='#000000', command=depupdatescr)
        self.dep_update_btn.place(x=470, y=235)
        self.dep_delete_btn = tk.Button(self.root, text='DELETE', font=('Yu Gothic UI Semibold', 12), bg='#ffe6e6', fg='#000000', command=depdelscr)
        self.dep_delete_btn.place(x=550, y=235)
        self.dep_show_btn = tk.Button(self.root, text='SHOW', font=('Yu Gothic UI Semibold', 12), bg='#73FBFD', fg='#000000', command=depshowscr)
        self.dep_show_btn.place(x=620, y=235)
        self.dep_check_btn = tk.Button(self.root, text='CHECK', font=('Yu Gothic UI Semibold', 12), bg='#73FBFD', fg='#000000', command=depcheckscr)
        self.dep_check_btn.place(x=690, y=235)
    def hide_dep_buttons(self):
        self.dep_save_btn.place_forget()
        self.dep_find_btn.place_forget()
        self.dep_update_btn.place_forget()
        self.dep_delete_btn.place_forget()
        self.dep_show_btn.place_forget()
        self.dep_check_btn.place_forget()
    
    def show_emp_buttons(self): 
        self.c1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#F08080',fg='#000000',command=empdatascr) 
        self.c1.place(x=350,y=280) 
        self.c2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#99FF66',fg='#000000',command=empfindscr) 
        self.c2.place(x=410,y=280) 
        self.c3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#fff',command=empupdatescr) 
        self.c3.place(x=470,y=280) 
        self.c4=Button(self.root,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=empdelscr) 
        self.c4.place(x=550,y=280) 
        self.c5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#ffe6e6',fg='#000000',command=empshowscr) 
        self.c5.place(x=620,y=280) 
        self.c6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=empcheckscr) 
        self.c6.place(x=690,y=280) 
    def hide_emp_buttons(self):
        self.c1.place_forget()
        self.c2.place_forget()
        self.c3.place_forget()
        self.c4.place_forget()
        self.c5.place_forget()
        self.c6.place_forget()
        
    def show_emp_sal_buttons(self): 
        self.d1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#ffff66',fg='#000000',command=empsalsave) 
        self.d1.place(x=350,y=325) 
        self.d2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#F08080',fg='#000000',command=empsalfind) 
        self.d2.place(x=410,y=325) 
        self.d3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#99FF66',fg='#000000',command=empsalupdate) 
        self.d3.place(x=470,y=325) #b4=Button(t,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#fff',command=empsaldel) #b4.place(x=550,y=340) 
        self.d5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=empsalshow) 
        self.d5.place(x=550,y=325) 
        self.d6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#ffe6e6',fg='#000000',command=empsalcheck) 
        self.d6.place(x=620,y=325)
    def hide_emp_sal_buttons(self):
        self.d1.place_forget()
        self.d2.place_forget()
        self.d3.place_forget()
       # self.d4.place_forget()
        self.d5.place_forget()
        self.d6.place_forget()
        
    def show_emp_leave_buttons(self): 
        self.e1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#cd9898',fg='#000000',command=emplevsave) 
        self.e1.place(x=350,y=370) 
        self.e2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#ffff66',fg='#000000',command=emplevfind) 
        self.e2.place(x=410,y=370) 
        self.e3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#F08080',fg='#000000',command=emplevupdate) 
        self.e3.place(x=470,y=370) # b4=Button(t,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#99FF66',fg='#000000',command=emplevdel) # b4.place(x=550,y=390) 
        self.e5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#fff',command=emplevshow) 
        self.e5.place(x=550,y=370) 
        self.e6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=emplevcheck) 
        self.e6.place(x=620,y=370)
    def hide_emp_leave_buttons(self):
        self.e1.place_forget()
        self.e2.place_forget()
        self.e3.place_forget()
        #selfeb4.place_forget()
        self.e5.place_forget()
        self.e6.place_forget()
        
    def show_tax_buttons(self): 
        self.f1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#cd9898',fg='#000000',command=taxsavescr) 
        self.f1.place(x=350,y=415) 
        self.f2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#ffff66',fg='#000000',command=taxfindscr) 
        self.f2.place(x=410,y=415) 
        self.f3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#F08080',fg='#000000',command=taxupdatescr) 
        self.f3.place(x=470,y=415) #b4=Button(t,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#99FF66',fg='#000000',command=taxdelscr) #b4.place(x=550,y=415) 
        self.f5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#fff',command=taxshowscr) 
        self.f5.place(x=550,y=415) 
        self.f6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=taxcheckscr) 
        self.f6.place(x=620,y=415)
    def hide_tax_buttons(self):
        self.f1.place_forget()
        self.f2.place_forget()
        self.f3.place_forget()
        #selffb4.place_forget()
        self.f5.place_forget()
        self.f6.place_forget()
        
    def show_salary_buttons(self): 
        self.g1=Button(self.root,text='SAVE',font=('Yu Gothic UI Semibold',12),bg='#ffff66',fg='#000000',command=salsavescr) 
        self.g1.place(x=350,y=460) 
        self.g2=Button(self.root,text='FIND',font=('Yu Gothic UI Semibold',12),bg='#F08080',fg='#000000',command=salfindscr) 
        self.g2.place(x=410,y=460) 
        self.g3=Button(self.root,text='UPDATE',font=('Yu Gothic UI Semibold',12),bg='#99FF66',fg='#000000',command=salupdatescr) 
        self.g3.place(x=470,y=460) #b4=Button(t,text='DELETE',font=('Yu Gothic UI Semibold',12),bg='#BA281D',fg='#fff',command=saldelscr) #b4.place(x=550,y=460) 
        self.g5=Button(self.root,text='SHOW',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=salshowscr) 
        self.g5.place(x=550,y=460) 
        self.g6=Button(self.root,text='CHECK',font=('Yu Gothic UI Semibold',12),bg='#73FBFD',fg='#000000',command=salcheckscr) 
        self.g6.place(x=620,y=460)
    def hide_salary_buttons(self):
        self.g1.place_forget()
        self.g2.place_forget()
        self.g3.place_forget()
        #self.gb4.place_forget()
        self.g5.place_forget()
        self.g6.place_forget()
def main_dashboard():
    root = tk.Tk()
    app = PayrollSystem(root)
    root.mainloop()
