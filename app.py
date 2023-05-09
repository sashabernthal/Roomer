from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "123secret"

# TODO: Fill in methods and routes


@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        session["username"] = username
        if password != "123":
            flash("Invalid Password", "info")
            return render_template("login.html")
        else:
            return redirect(url_for("home"))

@app.route("/")
@app.route("/profile")
def profile():
    return
render_template("profile.html")

@app.route("/signup")
def profile():
    if "username" in session:
        return render_template("profile.html")
    else:
        return redirect(url_for("login"))

@app.route("/login")
def profile():
    return
render_template("login.html")

@app.route("/matches")
def profile():
    return
render_template("matches.html")

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged out", "info")
    return redirect(url_for("login"))

# @app.before_first_request
# def setup():
#     init_db()
    

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
