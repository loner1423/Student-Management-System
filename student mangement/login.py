from tkinter import *
from tkinter import messagebox
import sqlite3
from register import Register
from dashboard import Dashboard
from forgot_password import ForgotPassword

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Student Result Management System")
        self.root.geometry("400x400+500+200")
        self.root.config(bg="white")
        self.email = StringVar()
        self.password = StringVar()
        Label(root, text="Login", font=("goudy old style", 20, "bold"), bg="white", fg="#033054").pack(pady=20)
        Label(root, text="Email", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.email, font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Label(root, text="Password", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.password, show="*", font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Button(root, text="Login", command=self.login, bg="#2196f3", fg="white", font=("goudy old style", 15), cursor="hand2").pack(pady=10)
        Button(root, text="Register", command=self.open_register, bg="#4caf50", fg="white", font=("goudy old style", 12)).pack()
        Button(root, text="Forgot Password?", command=self.open_forgot, bg="white", fg="red", font=("goudy old style", 12, "underline")).pack(pady=5)
    def login(self):
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student WHERE email=? AND password=?", (self.email.get(), self.password.get()))
            row = cur.fetchone()
            if row:
                messagebox.showinfo("Success", "Login successful", parent=self.root)
                self.root.destroy()
                root2 = Tk()
                Dashboard(root2)
                root2.mainloop()
            else:
                messagebox.showerror("Error", "Invalid credentials", parent=self.root)
            con.close()
    def open_register(self):
        self.root.destroy()
        root2 = Tk()
        Register(root2)
        root2.mainloop()
    def open_forgot(self):
        self.root.destroy()
        root2 = Tk()
        ForgotPassword(root2)
        root2.mainloop()
if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()