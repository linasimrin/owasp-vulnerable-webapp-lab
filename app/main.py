from flask import Flask, render_template, request
from database import init_db, get_connection

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        conn = get_connection()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()

        conn.close()

    if user:
        return "<h1>Login erfolgreich!</h1><a href='/shop'>Zum Shop</a>"

    else:
        return "<h1>Login fehlgeschlagen!</h1><a href='/login'>Zurück</a>"

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
    products = conn.execute(
        f"SELECT * FROM products WHERE name LIKE '%{search}%'"
    ).fetchall()
    conn.close()

    return render_template("shop.html", products=products, search=search)

if __name__ == "__main__":
    app.run(debug=True)