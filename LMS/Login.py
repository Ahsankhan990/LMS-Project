import pyodbc
import tkinter as tk
from tkinter import messagebox
from Connection import Control
import Admin_Deshboard
from Admin_Deshboard import Admin
from Student_Deshboard import Student


class LMS:
    def __init__(self,root:tk.Tk):
        self.db= Control()
        self.win:tk.Tk = root
        self.win.title("LMS Register/Login")
        self.win.geometry("370x350")
        self.win.iconbitmap("images/icon_image.ico")
        self.win.configure(bg = "#208dc4")
        self.win.resizable(False, False)
        
        
        label1 = tk.Label(self.win, text = "Username: ", bg="#208dc4", fg="white")
        label1.grid(row=0, column=0, ipady=2, pady=20,ipadx=10)
        self.username_get = tk.Entry(self.win, width=30)
        self.username_get.grid(row=0, column=1, ipady=2, pady=20)
        
        label2=tk.Label(self.win, text = "Name: ", bg="#208dc4", fg="white")
        label2.grid(row=1, column=0, ipady=2, pady=20,ipadx=10)
        self.name_get = tk.Entry(self.win, width=30)
        self.name_get.grid(row=1, column=1, ipady=2, pady=20)


        label3 = tk.Label(self.win, text = "Password: ", bg="#208dc4", fg="white")
        label3.grid(row=2, column=0, ipady=2,pady=20,ipadx=10)
       
        
        self.show = tk.BooleanVar()
        self.passowrd_get = tk.Entry(self.win, show= "*", width=30)
        self.passowrd_get.grid(row=2, column=1, ipady=2,pady=20)
        # self.hashed_password = bcrypt.hashpw(self.passowrd_get.encode('utf-8'), bcrypt.gensalt())
        self.check = tk.Checkbutton(self.win, text="Show Password",bg="#208dc4", variable=self.show, command=self.password_show)
        self.check.grid(row=3, column=1)
        
        
        
        label4 = tk.Label(self.win, text="Role Admin/Student: ", bg="#208dc4", fg="white")
        label4.grid(row=4, column=0, ipady=2,pady=20,ipadx=10)
        self.role_get = tk.Entry(self.win, width=30)
        self.role_get.grid(row=4, column=1, ipady=2,pady=20)

        button1 = tk.Button(self.win, text="Register",  font= 12, bg="black", fg="white", width=12, bd=0, relief="ridge", command= self.Reg_User )
        button1.grid(row=5, column=0, pady=15, padx=30)
        
        button2 = tk.Button(self.win, text="Login",  font= 12,bg="black", fg="white", width=12, bd=0, relief="ridge", command=self.Login_User)
        button2.grid(row=5, column=1, pady=15, padx=10)
       
        # label5=tk.Label(self.win, text="Write only username and password for login ", bg="#208dc4", fg="white")
        # label5.grid(row=5, column=0)
    
    #-----End GUI-----

    def password_show(self):
        if self.show.get():
            self.passowrd_get.config(show="")
        else:
            self.passowrd_get.config(show="*") 
            

    
    def Reg_User(self):
        username = self.username_get.get()
        name = self.name_get.get()
        password = self.passowrd_get.get()
        role = self.role_get.get()
        
        if username == "" or name == "" or password == "" or role == "":
            messagebox.showinfo("Warning", "All fields are required")
            return
        
        try:
            if role == "student":
                self.db.cursor.execute("Insert into tblusers (username, name, password, role) values(?,?,?,?)", (username,name,password,role))
                self.db.conn.commit()
                self.db.conn.close()
                messagebox.showinfo("Message","Registration Succuessfull.")
            
                self.username_get.delete(0, tk.END)
                self.name_get.delete(0, tk.END)
                self.passowrd_get.delete(0, tk.END)
                self.role_get.delete(0, tk.END)
            else:
                messagebox.showerror("Warning","Role must be student")
            
            
        except Exception as e:
            messagebox.showerror("Error", "Registration faild{e}")
            
    
    # login method
    
    def Login_User(self):
        username = self.username_get.get()
        name = self.name_get.get()
        password = self.passowrd_get.get()
        role = self.role_get.get()
        
        if username == "" or password == "" :
            messagebox.showinfo("Warning", "Only Username and password fields are required")
            return

        try:
            self.db.cursor.execute("select role, name,id from tblusers where username=? and password=?",(username,password))
            result = self.db.cursor.fetchone()
            
            
            if result:
                role_check = result[0]
                name_check = result[1]
                id_check = result[2]
                print("Name: ", name_check)
                print("Role: ",role_check)
                print("Id",id_check)
                
                if role_check == "admin":
                    self.win.destroy()
                    win2 = tk.Tk()
                    Admin(win2,id_check, name_check, role_check)
                    
                elif role_check == "student":
                    self.win.destroy()
                    win2 = tk.Tk()
                    Student(win2, id_check, name_check, role_check)
                else:
                    messagebox.showerror("Login Failed", "Invalid Role")
                
            else:
                    messagebox.showerror("Login Failed", "Invalid Username and Password")
            
        except Exception as e:
            messagebox.showerror("Error","Login Failed")
            self.db.close()
        


    
if __name__ == '__main__':
    win = tk.Tk()
    LMS(win)
    win.mainloop()



