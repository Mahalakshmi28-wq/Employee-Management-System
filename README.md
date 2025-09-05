# 🚀 Employee Management System

## 📌 Overview
The **Employee Management System** is a lightweight web application built with **Flask** and **MySQL** that allows organizations to manage employee records efficiently.  

Admins can log in, view all employees, add new records, edit details, and delete employees. The project demonstrates full **CRUD operations**, authentication, and session handling in a clean web interface.

---

## 🛠 Tech Stack
- **Backend:** Python (Flask)
- **Database:** MySQL (mysql-connector-python)
- **Frontend:** HTML, CSS, Jinja2 templates (Bootstrap optional)
- **Runtime:** Python 3.x

---

## ✨ Features
✔️ Secure Admin login (hardcoded for demo: `admin123 / admin123`)  
✔️ Employee login using **name or email**  
✔️ Full CRUD functionality:
- **Add Employee**
- **View Employee List**
- **Edit Employee**
- **Delete Employee**
✔️ Session-based authentication  
✔️ Clean UI with responsive tables  
✔️ Flash messages for user feedback  
✔️ Serial numbering in UI (even if database IDs skip after deletions)

---

## 📂 Project Structure
flask-app/
├── app.py # Main Flask app with routes
├── templates/
│ ├── login.html # Login page
│ ├── index.html # Dashboard (employee list)
│ ├── add_employee.html # Form to add new employee
│ └── edit_employee.html# Form to edit employee details
└── static/
└── images/
└── employee.png # Background / UI assets
