from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"   # needed for sessions

# ---------- Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="NewPassword123!",        # change if needed
        database="employee_db"
    )

# ---------- Login ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # ✅ Hardcoded Admin
        if username == "admin" and password == "admin123":
            session["user_id"] = 0
            session["user_name"] = "Administrator"
            session["job_title"] = "Admin"
            flash("Welcome Admin!", "success")
            return redirect(url_for("index"))

        # ✅ Check employees table
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM employees WHERE email=%s OR name=%s LIMIT 1", (username, username))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["job_title"] = user["job_title"]
            flash(f"Welcome {user['name']}!", "success")
            return redirect(url_for("index"))
        else:
            error = "Invalid credentials. Please try again."

    return render_template("login.html", error=error)

# ---------- Logout ----------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# ---------- Dashboard (READ) ----------
@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", employees=employees)

# ---------- Add Employee (CREATE) ----------
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        job_title = request.form["job_title"]
        salary = request.form["salary"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO employees (name, email, phone, job_title, salary) VALUES (%s, %s, %s, %s, %s)",
                    (name, email, phone, job_title, salary))
        conn.commit()
        cur.close()
        conn.close()

        flash("Employee added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_employee.html")

# ---------- Edit Employee (UPDATE) ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cur.fetchone()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        job_title = request.form["job_title"]
        salary = request.form["salary"]

        cur.execute("UPDATE employees SET name=%s, email=%s, phone=%s, job_title=%s, salary=%s WHERE id=%s",
                    (name, email, phone, job_title, salary, id))
        conn.commit()
        cur.close()
        conn.close()

        flash("Employee updated successfully!", "success")
        return redirect(url_for("index"))

    cur.close()
    conn.close()
    return render_template("edit_employee.html", employee=employee)

# ---------- Delete Employee (DELETE) ----------
@app.route("/delete/<int:id>")
def delete_employee(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    flash("Employee deleted successfully!", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
