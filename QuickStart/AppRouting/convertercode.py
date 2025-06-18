from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Welcome to the App,</h1> " \
    "<p>To see this work, add /user/yourusername to the URL.</p>" \
    "<p>Or you can try /hello</p>"

@app.route('/user/<username>')
def show_user(username):
    # Greet the user
    return f'Hello {username} !'

# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"

@app.route("/")
def index():
    return "Homepage of GeeksForGeeks"

if __name__ == "__main__":
    app.run(debug=True)