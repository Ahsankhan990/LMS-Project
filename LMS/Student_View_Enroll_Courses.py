from Connection import Control
import tkinter as tk
from tkinter import messagebox


class Student_View_Courses_Class:
    def __init__(self, root:tk.Tk ,std_id,std_name,role):
        self.std_id = std_id
        self.std_name = std_name
        self.role = role
        
        self.win = root
        self.db = Control()
        self.win.title(f"{std_name} Enroll Courses")
        self.win.geometry("350x300")
        self.win.iconbitmap("images/icon_image.ico")
        self.win.resizable(False,False)
        self.win.configure(bg="#208dc4")
        self.win.resizable(False, False)
        
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

        label1 = tk.Label(self.frame, text="Id",font=12 ,bg="white", fg="black")
        label1.grid(row=0, column=0, padx=20, pady=10)
        
        label2 = tk.Label(self.frame, text="Courses",font=12 ,bg="white", fg="black")
        label2.grid(row=0, column=1, padx=20, pady=10)
        
        button1=tk.Button(self.frame, text= "Back", bg="red", fg="white",width=14,height=3,command=lambda: self.back(self.std_id, self.std_name, self.role))
        button1.grid(row=0 , column=2, padx=15,pady=20)
        self.Get_Enroll_Courses(std_id)

    def Get_Enroll_Courses(self, std_id):
        
        self.db.cursor.execute("SELECT c.id, c.course_name FROM tblEnrollments e join tblcourses c on e.course_id = c.id WHERE e.users_id = ?", (std_id))     
        enrolled = self.db.cursor.fetchall()
        
    
        if not enrolled:
            label=tk.Label(self.frame, text="No courses enrolled yet.",font=12, bg="#208dc4", fg="white")
            label.grid(row=1, column=0, padx=10, pady=10)
        else:
            for i, course in enumerate(enrolled):
                course_id, course_name = course
                
                label3= tk.Label(self.frame, text=course_id, bg="#208dc4", fg="white", font=8)
                label3.grid(row=i+2, column=0, padx=20, pady=5)
                
                label4=tk.Label(self.frame, text=course_name, bg="#208dc4", fg="white", font=8)
                label4.grid(row=i+2, column=1, padx=20, pady=5)
        
    def back(self,std_id, std_name, role):
        self.win.destroy()
        win2 = tk.Tk()
        import Student_Deshboard
        Student_Deshboard.Student(win2,std_id,std_name,role)
