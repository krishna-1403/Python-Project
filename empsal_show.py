import tkinter as tk
import pymysql

def empsalshow():
    t = tk.Tk()
    t.geometry('800x800')
    
    # Create header labels
    headers = ["EmpID", "CT", "Var", "Slab", "Grade"]
    for idx, text in enumerate(headers):
        header = tk.Label(t, text=text, font=("Arial", 10, "bold"), bg="lightgrey")
        header.grid(row=0, column=idx, padx=10, pady=5)

    def filldata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        sql = "SELECT empid, ct, var, slab, grade FROM empsal"
        cur.execute(sql)
        data = cur.fetchall()
        
        # Display data in the respective columns
        for row_idx, res in enumerate(data, start=1):
            for col_idx, val in enumerate(res):
                cell = tk.Label(t, text=val, font=("Arial", 10))
                cell.grid(row=row_idx, column=col_idx, padx=10, pady=5)

    filldata()
    t.mainloop()

#empsalshow()
