from flask import Flask, render_template, request
from database import init_db, get_connection

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/shop")
def shop():
    search = request.args.get("search", "")

    conn = get_connection()

    # Absichtlich unsicher für VULN-01 SQL-Injection
    query = f"SELECT * FROM products WHERE name LIKE '%{search}%'"

    products = conn.execute(query).fetchall()
    conn.close()

    return render_template("shop.html", products=products, search=search)

if __name__ == "__main__":
    app.run(debug=True)