from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

# define int function
@app.route('/vint/<int:age>')
def vint(age):
    return "I am %d years old " % age

# we run our code in debug mode
app.run(debug=True)