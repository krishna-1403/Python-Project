import tkinter as tk
import pymysql
from tkinter import messagebox
from tkcalendar import Calendar

def fetch_data():
    try:
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        sql = "select empid, name, address, doj, phn, design, depid from empdata"
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        db.close()
        return data
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        return []

def empshowscr():
    t = tk.Tk()
    t.geometry('800x800')

    headers = ["EmpID", "Name", "Address", "DOJ", "Phone", "Design", "DepID"]
    for idx, text in enumerate(headers):
        header = tk.Label(t, text=text, font=("Arial", 10, "bold"), bg="lightgrey")
        header.grid(row=0, column=idx, padx=10, pady=5)

    def filldata():
        data = fetch_data()
        for row_idx, res in enumerate(data, start=1):
            for col_idx, val in enumerate(res):
                cell = tk.Label(t, text=val, font=("Arial", 10))
                cell.grid(row=row_idx, column=col_idx, padx=10, pady=5)

    filldata()
    t.mainloop()

#empshowscr()
