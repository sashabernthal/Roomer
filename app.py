from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "123secret"

# TODO: Fill in methods and routes


@app.route("/", methods = ["GET", "POST"])
def login():
    user = db_session.query(User).first()
    print(user)
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
            db_session.commit()
            return render_template("profile.html", user=user)


@app.route("/profile", methods=["Get", "POST"])
def profile():
    user = db_session.query(User).first()
    if "username" in session:
        print("user in session")
        user = db_session.query(User).filter(User.username == session["username"]).first()
        if user:
            return render_template("profile.html", user=user)
    print("user not in session")
    return render_template("profile.html", user=user)


@app.route("/matches")
def matches():
    return render_template("matches.html")

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged out", "info")
    return redirect(url_for("login"))

# @app.before_first_request
# def setup():
#     init_db()
    

@app.route("/signup", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        if password != confirm_password:
            print("Error: Passwords do not match.")
            return False
        user_exists = db_session.query(User).filter(User.username == request.form["username"]).first()
        if user_exists:
            print("Error: Username already exists.")
            return False
        interest_container = {
            "sports": False,
            "music": False,
            "traveling": False,
            "reading": False,
            "art": False,
            "dance": False,
            "video-games": False,
            "working-out": False,
            "cooking": False,
        }
        for interest in interest_container:
            if interest in request.form:
                interest_container[interest] = True
        new_user = User(
            username=request.form["username"],
            password=request.form["password"],
            name=request.form["name"],
            gender=request.form["gender"],
            university=request.form["university"],
            bio=request.form["bio"],
            sports=interest_container["sports"],
            music=interest_container["music"],
            traveling=interest_container["traveling"],
            reading=interest_container["reading"],
            art=interest_container["art"],
            dance=interest_container["dance"],
            video_games=interest_container["video-games"],
            working_out=interest_container["working-out"],
            cooking=interest_container["cooking"],
        )
        db_session.add(new_user)
        db_session.commit()

        session["username"] = new_user.username
        return redirect(url_for("profile"))
    else:
        return render_template("signup.html")
    
if __name__ == "__main__":
    init_db()
    # app.run(host="172.16.7.243", port="5001")
    app.run(debug=True)
