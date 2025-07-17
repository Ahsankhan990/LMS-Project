

 Learning Management System (LMS)

This is a basic Learning Management System (LMS) built with Python and Tkinter.

#) It includes:

* Login/Register system
* Admin Dashboard to manage courses and enrollments
* Student Dashboard to view and enroll in courses
* MySQL/SQL Server Database connection

#) Features:

* Add/Edit/Delete courses (Admin)
* Student course enrollment
* View student enrollments
* Export data to Excel


#) Technologies and Concepts Used

**Python 3**
- **Tkinter** for GUI
- **SQL Server** as Database
- **openpyxl** for Excel export
- **Exception Handling**
- **Object-Oriented Programming (OOP)**:
  - Custom classes for each window/page
- **Multi-File Project Structure**:
  - Each module (Login, Admin, Student, Database) is in a separate file
- **Database Connectivity**:
  - pyodbc used for connecting Python with SQL Server
- **Form Validation**:
  - Input checking for registration, login, course forms, etc.
- **Excel Export**:
  - Admin can export enrollments using openpyxl


#) How to Run:

1. Clone or download the repo
2. Import the SQL `.bak` file in SQL Server
3. Run `login.py` to start the app
4. You can see password of admin from database.

#) Database:

The database backup file `LMS_DB.bak` is included in this repo. Restore it using SQL Server.

#) Author:

Ahsan Khan

