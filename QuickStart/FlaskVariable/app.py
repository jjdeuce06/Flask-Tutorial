from flask import Flask
app = Flask(__name__)


@app.route('/')
def msg():
    return "Welcome To Encompass Remote!"

# we run code in debug mode
app.run(debug=True)