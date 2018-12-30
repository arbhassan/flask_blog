from flask import Flask, render_template, url_for
app = Flask(__name__)

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