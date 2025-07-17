import tkinter as tk
from tkinter import messagebox
from Connection import Control 
from Edit_Courses import Admin_Edit_Courses



class Admin_View_Class:
    def __init__(self, root:tk.Tk, admin_id, admin_name,role):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.role = role
        
        self.win = root
        self.db = Control()
        self.win.title("Admin Added Courses")
        self.win.geometry("400x400")
        self.win.resizable(False,False)
        self.win.configure(bg="#208dc4")
        self.win.iconbitmap("images/icon_image.ico")
        
        self.frame = tk.Frame(self.win, bg="#208dc4")
        self.frame.pack()
        self.Get_Courses()
        
    
    def Get_Courses(self):
        self.db.cursor.execute("select id, course_name from tblcourses")
        courses = self.db.cursor.fetchall()
       
        
        for remove in self.frame.winfo_children():
            remove.destroy()
        
        label1=tk.Label(self.frame, text="Courses",font=12 ,bg="#208dc4", fg="white")
        label1.grid(row=0, column=0, padx=10, pady=10)
        
        label2=tk.Label(self.frame, text="Id",font=12 ,bg="#208dc4", fg="white")
        label2.grid(row=1, column=0, padx=10, pady=10)
        
        label3=tk.Label(self.frame, text="Courses",font=12 ,bg="#208dc4", fg="white")
        label3.grid(row=1, column=1, padx=10, pady=10)
        
        button1=tk.Button(self.frame, text= "Back", bg="red", fg="white",width=18,height=3,command=lambda: self.back(self.admin_id, self.admin_name, self.role))
        button1.grid(row=0 , column=1,padx=10,pady=20)
        
        
        for i, course in enumerate(courses):
            course_id, course_name =  course
            
            label4=tk.Label(self.frame, text=(course_id), font=8)
            label4.grid(row=i+2, column=0 ,pady=5)
            
            label5=tk.Label(self.frame, text=(course_name), font=8)
            label5.grid(row=i+2, column=1 ,pady=5)
            
            button2=tk.Button(self.frame, text="Edit", bg="blue", fg="white",font=8, command=lambda: self.edit_course(course_id,self.admin_id, self.admin_name, self.role))
            button2.grid(row=i+2, column=2,padx=5,pady=5)
            
            button3=tk.Button(self.frame, text="Delete", bg="red",fg="white", font=8, command=lambda c_id=course_id: self.delete_course(c_id))
            button3.grid(row=i+2, column=3,padx=5,pady=5)
            
    def back(self,admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        import Admin_Deshboard
        Admin_Deshboard.Admin(win2,admin_id, admin_name,role)
    
    def delete_course(self, course_id):
        confirm = messagebox.askyesno("Confirm", "Confirm you want to delete this course")
        if confirm:
            try:
                self.db.cursor.execute("delete from tblcourses where id=?",(course_id,))
                self.db.conn.commit()
                self.Get_Courses()
            except Exception as e:
                messagebox.showerror("error","Not deleted")
            
    def edit_course(self, course_id,admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        Admin_Edit_Courses(win2,course_id,admin_id, admin_name,role)
        




