from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "secret_key"

# Create Database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")

conn.commit()
conn.close()

# Registration
@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, hashed)
            )

            conn.commit()

            return redirect('/login')

        except:
            return "User already exists"

    return render_template("register.html")

# Login
@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        if user:

            stored_password = user[2]

            if bcrypt.checkpw(
                password.encode('utf-8'),
                stored_password
            ):
                session['user'] = username
                return redirect('/dashboard')

        return "Invalid Credentials"

    return render_template("login.html")

# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'user' in session:
        return render_template(
            "dashboard.html",
            username=session['user']
        )

    return redirect('/login')

# Logout
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)