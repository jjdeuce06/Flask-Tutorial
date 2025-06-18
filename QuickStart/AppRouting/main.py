from flask import Flask

app = Flask(__name__)

# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to Encompass Remote!"
@app.route("/")
def index():
    return "Homepage of Encompass Remote!"

if __name__ == "__main__":
    app.run(debug=True)