import tkinter
import pymysql
from tkinter import *

st = ''

def taxshowscr():
    t = tkinter.Tk()
    t.geometry('800x800')
    
    headers = ["EmpID", "DepID", "CTC", "Tax", "Net Amt"]
    for idx, text in enumerate(headers):
        header = Label(t, text=text, font=("Arial", 10, "bold"), bg="lightgrey")
        header.grid(row=0, column=idx, padx=10, pady=5)

    global st
    def filldata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        sql = "select empid,depid,ctc,tax,netamt from tax"
        cur.execute(sql)
        data = cur.fetchall()
        
        for row_idx, res in enumerate(data, start=1):
            for col_idx, val in enumerate(res):
                cell = Label(t, text=val, font=("Arial", 10))
                cell.grid(row=row_idx, column=col_idx, padx=10, pady=5)

    filldata()
    t.mainloop()

#taxshowscr()
