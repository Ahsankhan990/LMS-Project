from Connection import Control
import tkinter as tk
from tkinter import messagebox
from Admin_Add_Courses import Admin_Add_Courses
from Admin_View_Courses import Admin_View_Class
from Admin_View_Enrollment import Admin_View_Enrollment_Class


class Admin:
    def __init__(self,root:tk.Tk,admin_id, admin_name,role ):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.role = role
        
        self.win = root 
        self.win.title( f"{admin_name} Admin Deshboard ")
        self.win.iconbitmap("images/icon_image.ico")
        self.win.geometry("330x330")
        self.win.configure(bg = "#208dc4")
        self.win.resizable(False, False)
        
        label1=tk.Label(self.win, text=f"Welcom to {admin_name} {role}", fg="black",bg="#ffffff",font=12)
        label1.grid(row=0 , column=0, pady=20)
        
        button1=tk.Button(self.win, text= "Add Courses", bg="black",font=12, fg="white",width=12,height=3,command=lambda: self.Add(self.admin_id, self.admin_name, self.role))
        button1.grid(row=1 , column=0,pady=20)
       
        button2=tk.Button(self.win, text= "View Courses", bg="black",font=12, fg="white",width=12,height=3,command=lambda: self.view(self.admin_id, self.admin_name, self.role))
        button2.grid(row=1 , column=1,pady=20)
       
        button3=tk.Button(self.win, text= "Enroll Courses", bg="black",font=12, fg="white",width=12,height=3, command=lambda: self.view_Enroll(self.admin_id, self.admin_name, self.role))
        button3.grid(row=2 , column=0, padx=20,pady=20)
        
        button4=tk.Button(self.win, text= "Back", bg="red",font=12, fg="white",width=12,height=3,command=self.back)
        button4.grid(row=2 , column=1,pady=20)

    
    def back(self):
        self.win.destroy()
        import Login 
        
        win2 = tk.Tk()
        Login.LMS(win2)
      
        
    def Add(self,admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        Admin_Add_Courses(win2,admin_id, admin_name,role)
        
    def view(self, admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        Admin_View_Class(win2, admin_id, admin_name,role)


    def view_Enroll(self, admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        Admin_View_Enrollment_Class(win2, admin_id, admin_name,role)

# win = tk.Tk()
# app = Admin(win)
# win.mainloop()

