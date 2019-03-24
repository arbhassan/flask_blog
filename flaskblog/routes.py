from flask import render_template, url_for, flash, redirect
from flaskblog import APP
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

POSTS = [
    {
        "author": "Arbab Hassan",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Dec 29, 2018",
    },
    {
        "author": "Zalaan Khan",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "Dec 30, 2018",
    },
]


@APP.route("/")
@APP.route("/home")
def home():
    return render_template("home.html", posts=POSTS)


@APP.route("/about")
def about():
    return render_template("about.html", title="About")


@APP.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@APP.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
