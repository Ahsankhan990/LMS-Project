import pyodbc
from tkinter import messagebox

class Control:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DESKTOP-88EQMC0\\SQLEXPRESS;'
                'DATABASE=LMS;'
                'Trusted_Connection=yes;'
            )

            self.cursor = self.conn.cursor()
            
        except Exception as e:
            messagebox.showerror("Error", "Connection failed", str({e}))
        
    def close(self):
        self.conn.close()