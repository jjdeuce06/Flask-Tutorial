
# 🧩 Template Inheritance in Flask with Jinja2

Template inheritance is a core feature of Jinja (Flask's templating engine) that promotes code reuse and a clean structure.

## 📌 What Is Template Inheritance?

It allows you to define a **base structure** (like header, footer, navbar) once in a **base template** and reuse it across multiple pages.

### 🌟 Benefits
- **Code Reusability**: Avoid duplicating common HTML.
- **Maintainability**: Change the layout in one place (base template).
- **Separation of Concerns**: Split structure and content clearly.
- **Scalability**: Easily add new pages with consistent layouts.

---

## 🚀 Implementation Steps

### Step 1: Set Up Flask App

Create `app.py` in a folder (e.g., `TemplateInheritance`) and define basic routes.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Step 2: Create `base.html`

Place this in the `templates` folder.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>My Flask Website</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a>
    </nav>
    <hr>
    {% block content %}
    {% endblock %}
</body>
</html>
```

### Step 3: Create Child Templates

These templates extend `base.html` and override the `content` block.

#### `home.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Welcome to the Home Page</h2>
<p>This page inherits from base.html</p>
{% endblock %}
```

#### `about.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>About Us</h2>
<p>This is the about page content.</p>
{% endblock %}
```

---

## 🏃 Running the Application

1. Place `base.html`, `home.html`, and `about.html` in the `templates/` folder.
2. Run the app:
```
python app.py
```
3. Open in your browser:
- [Home Page](http://127.0.0.1:5000/)
- [About Page](http://127.0.0.1:5000/about)

---

## ⚙️ How It Works

- Flask renders different views (`home.html`, `about.html`) for each route.
- Each template **inherits** from `base.html`.
- The `{% block content %}` area in `base.html` is **replaced** by the content block in the specific page.

This ensures a **consistent layout** and easy content management across pages.
