from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

# We defined string  function
@app.route('/vstring/<name>')
def string(name):
    return "My Name is %s" % name

# we run app debugging mode
app.run(debug=True)