# AI assistance: ChatGPT was used to help explain and debug parts of this project.

from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "expense-tracker-secret-key"

db = SQL("sqlite:///expenses.db")


@app.route("/")
def index():
    if "user_id" not in session:
        return render_template("index.html")

    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY created_at DESC",
        session["user_id"]
    )

    income = db.execute(
        "SELECT SUM(amount) AS total FROM transactions WHERE user_id = ? AND type = 'income'",
        session["user_id"]
    )[0]["total"] or 0

    expenses = db.execute(
        "SELECT SUM(amount) AS total FROM transactions WHERE user_id = ? AND type = 'expense'",
        session["user_id"]
    )[0]["total"] or 0

    balance = income - expenses

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expenses=expenses,
        balance=balance
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return "Username is required"

        if not password:
            return "Password is required"

        if password != confirmation:
            return "Passwords do not match"

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username,
                generate_password_hash(password)
            )
        except ValueError:
            return "Username already exists"

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"],
            password
        ):
            return "Invalid username or password"

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        description = request.form.get("description")
        amount = request.form.get("amount")
        category = request.form.get("category")

        if not description or not amount or not category:
            return "All fields are required"

        try:
            amount = float(amount)
        except ValueError:
            return "Invalid amount"

        if amount <= 0:
            return "Amount must be greater than zero"

        db.execute(
            """
            INSERT INTO transactions
            (user_id, type, category, description, amount)
            VALUES (?, ?, ?, ?, ?)
            """,
            session["user_id"],
            "expense",
            category,
            description,
            amount
        )

        return redirect("/")

    return render_template("add.html")


@app.route("/income", methods=["GET", "POST"])
def income():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        description = request.form.get("description")
        amount = request.form.get("amount")

        if not description or not amount:
            return "All fields are required"

        try:
            amount = float(amount)
        except ValueError:
            return "Invalid amount"

        if amount <= 0:
            return "Amount must be greater than zero"

        db.execute(
            """
            INSERT INTO transactions
            (user_id, type, category, description, amount)
            VALUES (?, ?, ?, ?, ?)
            """,
            session["user_id"],
            "income",
            "Income",
            description,
            amount
        )

        return redirect("/")

    return render_template("income.html")
@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete(transaction_id):
    if "user_id" not in session:
        return redirect("/login")

    db.execute(
        "DELETE FROM transactions WHERE id = ? AND user_id = ?",
        transaction_id,
        session["user_id"]
    )

    return redirect("/")
