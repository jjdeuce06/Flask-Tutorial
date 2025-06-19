from flask import Flask, render_template

#Initializes the Flask Application
app = Flask(__name__)

#Maps the root URL to the index function
@app.route("/")
def index():
    #Renders the index.html template
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("about.html", sites=sites)

@app.route("/contact/<role>")
def contact(role):
    return render_template("contact.html", person=role)

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)

if __name__ == "__main__":
    app.run()
    #starts the server