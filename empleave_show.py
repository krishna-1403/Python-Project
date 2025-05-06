import tkinter
from tkinter import *
from tkinter import ttk
import pymysql


def emplevshow():
    # Function to fetch data from the database based on empid
    def fetch_data(empid):
        # Connect to the database
        db = pymysql.connect(host='localhost', user='root', password='root', database='eps')
        cur = db.cursor()
        
        # Execute the query
        cur.execute("SELECT month, noleave, type FROM empleave WHERE empid = %s", (empid,))
        
        # Fetch all the rows
        rows = cur.fetchall()
        
        # Close the connection
        db.close()
        
        return rows
    
    # Function to display data in the Treeview
    def display_data():
        empid = entry_empid.get()
        data = fetch_data(empid)
        
        # Clear the Treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Insert the data into the Treeview
        for row in data:
            tree.insert("", END, values=row)
    
    # Create the main window
    root = Tk()
    root.title("Data Table")
    root.geometry("600x400")
    
    # Create a frame for the Treeview
    frame = Frame(root)
    frame.pack(pady=20)
    
    # Create a Treeview widget
    tree = ttk.Treeview(frame, columns=("month", "noleave", "type"), show='headings', height=8)
    
    # Define the column headings
    tree.heading("month", text="ID")
    tree.heading("noleave", text="Name")
    tree.heading("type", text="City")
    
    
    # Define the column widths
    tree.column("month", width=100, anchor=CENTER)
    tree.column("noleave", width=150, anchor=CENTER)
    tree.column("type", width=150, anchor=CENTER)
    
    
    # Add a scrollbar
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack()
    
    # Create an entry box for empid
    label_empid = Label(root, text="Enter Employee ID:")
    label_empid.pack(pady=5)
    entry_empid = Entry(root)
    entry_empid.pack(pady=5)
    
    # Create a button to fetch and display data
    button_fetch = Button(root, text="Fetch Data", command=display_data)
    button_fetch.pack(pady=10)
    
    # Run the application
    root.mainloop()