import tkinter as tk
from tkinter import messagebox
from Connection import Control 



class Admin_Add_Courses:
    def __init__(self, root:tk.Tk,admin_id, admin_name,role):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.role = role
        
        self.win = root
        self.db = Control()
        self.win.title("Admin Add Courses")
        self.win.geometry("350x300")
        self.win.iconbitmap("images/icon_image.ico")
        self.win.resizable(False,False)
        self.win.configure(bg="#208dc4")
        self.win.resizable(False, False)
        
        tk.Label(self.win, bg="#208dc4", text="Add Courses", font=12).grid(row=0, column=0, padx=20, pady=10 )
        self.add_course = tk.Entry(self.win, width=30, font=10)
        self.add_course.grid(row=1, column=0, padx=20, pady=20)
        
        tk.Button(self.win,text="Add Courses", bg="black", fg="white", width=20,font=10, command=self.db_add).grid(row=2, column=0, padx=40, pady=10)
        tk.Button(self.win, text= "Back", bg="red", fg="white",width=18,height=3,command=lambda: self.back(self.admin_id, self.admin_name, self.role)).grid(row=3 , column=0,padx=40,pady=20)
        
        
    def back(self,admin_id, admin_name,role):
        self.win.destroy()
        import Admin_Deshboard
        
        win2 = tk.Tk()
        Admin_Deshboard.Admin(win2,admin_id, admin_name,role)
        
    def db_add(self):
        course = self.add_course.get()
        cap_course = course.upper()
        
            
        if course == "":
            messagebox.showinfo("warning","Plz Write Coure name")
            return
        
        try:
            self.db.cursor.execute("select course_name from tblcourses")
            result =  self.db.cursor.fetchall()
            
            course_list = [row[0] for row in result]
            
            if cap_course in course_list:
                messagebox.showwarning("Warning","You have already add this course")
            else:
                self.db.cursor.execute("insert into tblcourses(course_name) values(?)",(cap_course))
                self.db.conn.commit()
                messagebox.showinfo("message","Course Add Successfull")
        
            
        except Exception as e:
            messagebox.showerror("error","Course Not added",e)

# win = tk.Tk()
# Admin_Add_Courses(win,1,"ahsan","admin")
# win.mainloop()