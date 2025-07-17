import tkinter as tk
from tkinter import messagebox
from Connection import Control 


class Student_Enroll_Class:
    def __init__(self, root:tk.Tk, std_id, std_name, role):
        self.std_id = std_id
        self.std_name = std_name
        self.role = role
        
        
        self.win = root
        self.db = Control()
        self.win.title(f"{std_name} Avaibale Courses")
        self.win.geometry("400x300")
        self.win.resizable(False,False)
        self.win.configure(bg="#208dc4")
        self.win.iconbitmap("images/icon_image.ico")
        
        outer_frame = tk.Frame(self.win)
        outer_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(outer_frame, bg="#208dc4")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(outer_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.frame = tk.Frame(canvas, bg="#208dc4")
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.Get_Courses(std_id)
        
     
        
        label1=tk.Label(self.frame, text="Available Courses", font=8)
        label1.grid(row=0, column=1)
        # tk.Label(self.frame2, text="Enrolled Courses").grid(row=0, column=0)
    
    
    
    def Get_Courses(self,std_id):
        self.db.cursor.execute("select id, course_name from tblcourses")
        courses = self.db.cursor.fetchall()
       
        
        for remove in self.frame.winfo_children():
            remove.destroy()
        
        # tk.Label(self.frame, text="Courses",font=12 ,bg="#208dc4", fg="white").grid(row=1, column=0, padx=20, pady=10)
        label2=tk.Label(self.frame, text="Id",font=12 ,bg="#208dc4", fg="white")
        label2.grid(row=1, column=0, padx=20, pady=10)
        
        label3=tk.Label(self.frame, text="Courses",font=12 ,bg="#208dc4", fg="white")
        label3.grid(row=1, column=1, padx=20, pady=10)
        
        button1=tk.Button(self.frame, text= "Back", bg="red", fg="white",width=7,height=3,command=lambda: self.back(self.std_id, self.std_name, self.role))
        button1.grid(row=0 , column=2,padx=40,pady=20)
        
        
        for i, course in enumerate(courses):
            course_id, course_name =  course
            
            label4=tk.Label(self.frame, text=(course_id), font=8)
            label4.grid(row=i+2, column=0 ,pady=5)
            
            label5=tk.Label(self.frame, text=(course_name), font=8)
            label5.grid(row=i+2, column=1 ,pady=5)
            
            button2=tk.Button(self.frame, text="Enroll", bg="blue", fg="white",font=8, command=lambda c=course_id: self.Enroll(c, std_id))
            button2.grid(row=i+2, column=2,padx=5,pady=5)
        
    
    def Enroll(self, course_id, std_id):
        try:
            self.db.cursor.execute("select * from tblEnrollments where users_id = ? and course_id = ?",(std_id,course_id))
            Check_Enroll_Course = self.db.cursor.fetchone()
            
            if Check_Enroll_Course:
                messagebox.showwarning("Warning", "Student has already this course")
            else:    
                self.db.cursor.execute("insert into tblEnrollments(users_id,course_id,enrollment_Date) values(?,?,GETDATE())",(std_id,course_id))
                messagebox.showinfo("Message","Course Successfully Enrolled")
                self.db.cursor.commit()
            
        except Exception as e:
            messagebox.showerror("Error", "Not Enrolled")
        
    def back(self,std_id, std_name, role):
        self.win.destroy()
        win2 = tk.Tk()
        import Student_Deshboard
        Student_Deshboard.Student(win2,std_id,std_name,role)




