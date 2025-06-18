from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Welcome to the App,</h1> " \
           "<p>To see this work, add /user/yourusername to the URL.</p>" \

def show_user(username):
    # Greet the user
    return f'Hello {username} !'
app.add_url_rule('/user/<username>', 'show_user', show_user)

if __name__ == "__main__":
    app.run(debug=True)