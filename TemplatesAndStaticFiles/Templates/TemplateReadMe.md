
# Flask Template Rendering Guide

This project demonstrates how to use templates with Flask using Jinja2 for dynamic content generation.

## 🛠️ Setting up Flask

### Create and Activate Virtual Environment
```
python -m venv venv
```

#### Activate (OS-specific):
- **Windows:** `venv\Scripts\activate`
- **Linux/macOS:** `venv/bin/activate`

### Install Flask
```
pip install flask
```

## 🚀 Creating the Application

Ensure `app.py` exists and routes are properly defined.

## 🧩 Rendering HTML Templates

Flask supports HTML template rendering with `render_template()` using Jinja2.

### Create `templates` Folder

Ensure your `index.html` and other templates are inside a `templates/` directory.

## 🧱 Templating with Jinja2 in Flask

### Dynamic Routing with Parameters

```python
@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)
```

This captures a name from the URL and passes it to the template.

## 🧬 Jinja Template Inheritance

Instead of copying layout code, use inheritance.

### Base Template (`index.html`)
```html
{% block body %}
<p>This is a Flask application.</p>
{% endblock %}
```

### Extending Template (`home.html`)
```html
{% extends 'index.html' %}
{% block body %}
<p>This is a home page</p>
{% endblock %}
```

### Route for `home.html`
```python
@app.route("/home")
def home():
    return render_template("home.html")
```

## 🧠 Inducing Logic in Templates

### Using For Loops

```python
@app.route("/about")
def about():
    sites = ["Facebook", "Twitter", "Instagram"]
    return render_template("about.html", sites=sites)
```

#### about.html:
```html
{% extends 'index.html' %}
{% block body %}
<ul>
  {% for social in sites %}
    <li>{{ social }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

## 🔁 If Statement in Templates

### Route:
```python
@app.route("/contact/<role>")
def contact(role):
    return render_template("contact.html", person=role)
```

### contact.html:
```html
{% if person == 'admin' %}
<p>Welcome, Admin!</p>
{% elif person == 'user' %}
<p>Welcome, User!</p>
{% else %}
<p>Role not recognized.</p>
{% endif %}
```

## 🔗 Accessing Contact Route

Since the contact route takes a dynamic role, access it via URL manually:
```
http://localhost:5000/contact/admin
```

---

This project is split into `FirstExample` and `SecondExample` folders to demonstrate different template functionalities in Flask.
