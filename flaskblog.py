from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>This is freaking awesome!</h1>"
    

@app.route("/about")
def about():
    return "<h1>About Page</h1>"