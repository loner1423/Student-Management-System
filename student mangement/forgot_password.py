from tkinter import *
from tkinter import messagebox
import sqlite3

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("400x350+500+200")
        self.root.config(bg="white")
        self.email = StringVar()
        self.new_pass = StringVar()
        Label(root, text="Forgot Password", font=("goudy old style", 20, "bold"), bg="white", fg="#033054").pack(pady=20)
        Label(root, text="Email", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.email, font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Label(root, text="New Password", font=("goudy old style", 15), bg="white").pack(pady=5)
        Entry(root, textvariable=self.new_pass, show="*", font=("goudy old style", 15), bg="lightyellow").pack(pady=5)
        Button(root, text="Reset Password", command=self.reset_password, bg="#4caf50", fg="white", font=("goudy old style", 15)).pack(pady=20)
        Button(root, text="Back to Login", command=self.back_to_login, bg="#2196f3", fg="white", font=("goudy old style", 12)).pack()
    def reset_password(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student WHERE email=?", (self.email.get(),))
        row = cur.fetchone()
        if not row:
            messagebox.showerror("Error","Email not found", parent=self.root)
        else:
            cur.execute("UPDATE student SET password=? WHERE email=?", (self.new_pass.get(), self.email.get()))
            con.commit()
            messagebox.showinfo("Success","Password updated successfully", parent=self.root)
            self.back_to_login()
        con.close()
    def back_to_login(self):
        self.root.destroy()
        from login import Login
        root2 = Tk()
        Login(root2)
        root2.mainloop()