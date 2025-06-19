
# 🌐 Flask Web App Tutorial — Templates & Static Files

This guide walks you through building dynamic web applications using **Flask**, **Jinja2**, and **static files** like CSS, JavaScript, and media.

---

## 📑 Section 1: Templates in Flask

Templates are HTML files that Flask uses to render dynamic content. Flask uses **Jinja2** as the default templating engine.

### 🔧 Setup & Example
1. Create a `templates/` folder in your project.
2. Add HTML files like `index.html`, `home.html`, etc.
3. Use Jinja syntax like `{{ variable }}` and `{% if ... %}` for logic.

**Example:**
```python
@app.route("/")
def home():
    return render_template("index.html", message="Hello Flask")
```

**Jinja Usage in index.html:**
```html
<h1>{{ message }}</h1>
```

---

## 🧱 Section 2: Template Inheritance

Jinja2 supports **template inheritance** to avoid repeating common HTML structures like headers and footers.

### 👣 Steps
1. Create `base.html` with blocks like:
   ```html
   {% block content %}{% endblock %}
   ```
2. In other templates, extend the base:
   ```html
   {% extends "base.html" %}
   {% block content %}
   <p>This is the child content</p>
   {% endblock %}
   ```
3. Define routes in Flask to render these templates.

**Benefits:**
- Code Reusability
- Cleaner Layouts
- Easier Maintenance

---

## 🎨 Section 3: Static Files in Flask

Flask automatically serves static files from the `static/` folder.

### 📁 Structure Example:
```
/static
    style.css
    script.js
    cat.jpg
/templates
    index.html
    image.html
```

### 🛠️ How To Use

- **CSS**: Place in `/static/`, link via:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```
- **JavaScript**: Place in `/static/`, link via:
  ```html
  <script src="{{ url_for('static', filename='serve.js') }}"></script>
  ```
- **Media (Images, Video, Audio)**: Place in `/static/`, reference in HTML:
  ```html
  <img src="{{ url_for('static', filename='cat.jpg') }}" alt="Cat">
  ```

**Routes in Flask:**
```python
@app.route("/image")
def serve_image():
    return render_template("image.html")
```

---

## 🧪 Running the App

1. Make sure your file structure includes `templates/` and `static/` folders.
2. Run the app:
```
python main.py
```
3. Visit in browser:
- `http://localhost:5000/` — Home
- `http://localhost:5000/about` — About
- `http://localhost:5000/image` — Image route
- etc.

---

## 📝 Summary

| Feature              | Folder       | Usage                   |
|----------------------|--------------|--------------------------|
| Templates (HTML)     | `templates/` | `render_template()`     |
| Static Files (CSS/JS)| `static/`    | `url_for('static',...)` |
| Template Inheritance | `base.html`  | `{% extends %}`          |
| Dynamic Routes       | `app.py`     | `@app.route`            |

This structure promotes clean, scalable, and maintainable web applications.

Happy Coding! 🚀
