from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3a9bfdc8a927f9e656c54d8f06a43132'

posts = [
    {
        'author': 'Arbab Hassan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Dec 29, 2018'
    },
    {
        'author': 'Zalaan Khan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 30, 2018'
    },
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)
    

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)