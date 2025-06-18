from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

# define float function
@app.route('/vfloat/<float:balance>')
def vfloat(balance):
    return "My Account Balance %f" % balance

# we run our code in debugging mode
app.run(debug=True)