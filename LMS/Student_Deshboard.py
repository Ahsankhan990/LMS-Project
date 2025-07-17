from Connection import Control
import tkinter as tk
from tkinter import messagebox



class Student:
    def __init__(self,root:tk.Tk,std_id , std_name, role):
        self.std_name = std_name
        self.role = role
        self.std_id = std_id
        
        self.win = root 
        self.win.title( "Student Deshboard ")
        self.win.iconbitmap("images/icon_image.ico")
        self.win.geometry("300x300")
        self.win.configure(bg = "#208dc4")
        self.win.resizable(False, False)
        
        label1=tk.Label(self.win, text=f"Welcome to {self.std_name}", fg="black",bg="#ffffff",font=12)
        label1.grid(row=0 , column=0, padx=20,pady=20)
        
        button2=tk.Button(self.win, text= "Course Enroll", bg="black", fg="white",width=14,height=3, command=lambda: self.Course_Enroll(self.std_id,self.std_name,self.role))
        button2.grid(row=1 , column=0, padx=20,pady=20)
        
        button3=tk.Button(self.win, text= "View Enroll Courses", bg="black", fg="white",height=3,command=lambda: self.View_Enroll(self.std_id,self.std_name,self.role))
        button3.grid(row=3 , column=0, padx=20,pady=20)
        
        button4=tk.Button(self.win, text= "Logout", bg="red", fg="white",width=14,height=3,command=self.back)
        button4.grid(row=3 , column=1, padx=15,pady=20)

    def back(self):
        pass
        self.win.destroy()
        import Login 
        
        win2 = tk.Tk()
        Login.LMS(win2)
        
    
    def Course_Enroll(self, std_id, std_name, role):
        self.win.destroy()
        import Student_Enroll_Courses
        win2 = tk.Tk()
        Student_Enroll_Courses.Student_Enroll_Class(win2,std_id,std_name,role)
        

    def View_Enroll(self, std_id, std_name, role):
        self.win.destroy()
        import Student_View_Enroll_Courses
        win2 = tk.Tk()
        Student_View_Enroll_Courses.Student_View_Courses_Class(win2,std_id,std_name,role)
           

