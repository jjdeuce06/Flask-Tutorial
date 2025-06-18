# importing abort
from flask import Flask, abort

# Initialize the flask application
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome! Please enter a username in the URL using the format /<username> </h1>'

@app.route('/<uname>')
def index(uname):
    if uname[0].isdigit():
        abort(400)
    return '<h1>Good Username</h1>'


if __name__ == '__main__':
    app.run()