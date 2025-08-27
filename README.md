
# 🎓 Student Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green) ![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

## 📌 Overview

The **Student Management System** is a **Python-based desktop application** with a **Tkinter GUI** and a **SQLite database**.
It enables secure **login**, **student information management**, **course handling**, **result tracking**, and **report generation** for small institutions or personal projects.

---

## 📂 Project Structure

```
student-management-system/
│
├── course.py          # Handles course management
├── result.py          # Manages results and grades
├── dashboard.py       # Main dashboard for navigation
├── login.py           # Login and authentication system
├── report.py          # Generates student reports
├── student.py         # Manages student data (CRUD operations)
├── create-db.py       # Initializes the SQLite database (tables, schema)
├── rms.db             # SQLite database file (auto-generated after setup)
├── __pycache__/       # Python cache folder (ignored in Git)
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## 🧠 Features

✅ **Database Setup** – Create or reset the SQLite database using `create-db.py`
✅ **Login Authentication** – Secure admin or staff access
✅ **Student Management** – Add, edit, search, and delete student records
✅ **Course Management** – Manage course creation and details
✅ **Result Processing** – Input, update, and calculate student results
✅ **Report Generation** – Export student reports for reference
✅ **GUI Interface** – User-friendly and clean interface built with Tkinter

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
cd Student-Management-System
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### **1. Initialize the Database**

Run the script to create the `rms.db` file and set up tables:

```bash
python create-db.py
```

### **2. Start the Application**

Run the login interface to access the dashboard:

```bash
python login.py
```

---

## 🗂 Database Schema

| Table        | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| **Users**    | Admin login credentials                                     |
| **Students** | Basic student information (name, email, course, year, etc.) |
| **Courses**  | Course details and codes                                    |
| **Results**  | Marks and grades for students                               |
| **Reports**  | Data summaries for report generation                        |

---

## 📊 Example Workflow

1. Run `create-db.py` to set up the database.
2. Use `login.py` to log in as an admin.
3. Add new students via the **Student Management** module.
4. Enter results through `result.py`.
5. Generate detailed reports using `report.py`.

---

## 🛠 Tech Stack

* **Language:** Python 3.8+
* **GUI:** Tkinter
* **Database:** SQLite
* **Libraries:** sqlite3, tkinter, messagebox, pandas (optional for exports)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

## 🙌 Acknowledgements

* [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
* [SQLite Documentation](https://www.sqlite.org/docs.html)

---

Would you like me to **add screenshots or a setup GIF** to make the README more visually descriptive?
