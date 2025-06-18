# importing redirect
from flask import Flask, redirect, url_for, render_template, request

# Initialize the flask application
app = Flask(__name__)

# It will load the form template which 
# is in login.html
@app.route('/')
def index():
    return render_template("login.html")


@app.route('/success')
def success():
    return "logged in successfully"

@app.route('/fail')
def failure():
    return "login failed, please try again"

# loggnig to the form with method POST or GET
@app.route("/login", methods=["POST", "GET"])
def login():
    # if the method is POST and Username is admin then
    # it will redirects to success url.
    if request.method == "POST" and request.form["username"] == "admin":
        return redirect(url_for("success"))
    else:
        return redirect(url_for("failure"))

    # if the method is GET or username is not admin,
    # then it redirects to index method.
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)