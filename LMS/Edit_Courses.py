import tkinter as tk
from tkinter import messagebox
from Connection import Control 


class Admin_Edit_Courses:
    def __init__(self, root:tk.Tk, course_id,admin_id, admin_name,role):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.role = role
        
        self.win = root
        self.db = Control()
        self.win.title("Admin Add Courses")
        self.win.geometry("400x300")
        self.win.resizable(False,False)
        self.win.configure(bg="#208dc4")
        self.win.iconbitmap("images/icon_image.ico")
        
        
        tk.Label(self.win, bg="#208dc4", text="Edit Courses", font=8).grid(row=0, column=0, padx=10, pady=10 )
        self.update_course = tk.Entry(self.win, width=30, font=10)
        self.update_course.grid(row=1, column=0, padx=20, pady=20)
        
        tk.Button(self.win,text="Update Courses", bg="black", fg="white", width=15,font=10, command=lambda c_id=course_id: self.edit_course(c_id)).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.win, text= "Back", bg="red", fg="white",width=15,height=3,command=lambda: self.back(self.admin_id, self.admin_name, self.role)).grid(row=2 , column=1,padx=10,pady=10)
        
        
        
    def edit_course(self,course_id):
        course_name = self.update_course.get()
        if course_name == "":
            messagebox.showinfo("warning","Plz Write Update Course name")
        
        try:
            self.db.cursor.execute("update tblcourses set course_name=? where id=?",(course_name,course_id))
            self.db.conn.commit()
           
            messagebox.showinfo("message","Course Update Successfull")
     
            
        except Exception as e:
            messagebox.showerror("error","Course Not updated",e)


    def back(self,admin_id, admin_name,role):
        self.win.destroy()
        win2 = tk.Tk()
        import Admin_View_Courses
        Admin_View_Courses.Admin_View_Class(win2, admin_id, admin_name,role)
        
        

