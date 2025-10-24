from tkinter import *
from tkinter import messagebox
import sqlite3

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register - Student Result Management System")
        self.root.geometry("400x500+500+150")
        self.root.config(bg="white")
        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm = StringVar()
        Label(root, text="Register", font=("goudy old style", 20, "bold"), bg="white", fg="#033054").pack(pady=20)
        Label(root, text="Name", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.name, font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Label(root, text="Email", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.email, font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Label(root, text="Password", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.password, show="*", font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Label(root, text="Confirm Password", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.confirm, show="*", font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Button(root, text="Register", command=self.register_user, bg="#4caf50", fg="white", font=("goudy old style", 15)).pack(pady=20)
        Button(root, text="Back to Login", command=self.back_to_login, bg="#2196f3", fg="white", font=("goudy old style", 12)).pack()
    def register_user(self):
        if self.name.get()=="" or self.email.get()=="" or self.password.get()=="" or self.confirm.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.password.get()!=self.confirm.get():
            messagebox.showerror("Error","Passwords do not match", parent=self.root)
        else:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student WHERE email=?", (self.email.get(),))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error","Email already exists", parent=self.root)
            else:
                cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", (self.name.get(), self.email.get(), self.password.get()))
                con.commit()
                messagebox.showinfo("Success","Registration successful", parent=self.root)
                self.root.destroy()
                from login import Login
                root2 = Tk()
                Login(root2)
                root2.mainloop()
            con.close()
    def back_to_login(self):
        self.root.destroy()
        from login import Login
        root2 = Tk()
        Login(root2)
        root2.mainloop()