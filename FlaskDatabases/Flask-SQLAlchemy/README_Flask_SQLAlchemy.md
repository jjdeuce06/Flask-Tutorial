
# 🗃️ Flask-SQLAlchemy Integration

Flask doesn't include built-in support for databases, so it uses **SQLAlchemy**, a powerful ORM (Object Relational Mapper) that allows developers to interact with databases using Python classes instead of SQL queries.

---

## ✅ Why Use SQLAlchemy?
- Simplifies database operations
- Secures data handling
- Supports multiple databases like SQLite, MySQL, PostgreSQL
- Seamlessly integrates with Flask

---

## 🔧 Installation Steps

```bash
python -m venv venv
# Activate virtual environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install flask flask-sqlalchemy
```

---

## 📁 File Structure

Here’s what your project should look like:

![Flask-SQLAlchemy File Structure](flask_sqlalchemy_structure.png)

---

## 🚀 Setting Up `app.py`

In `app.py`:
```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
```

This sets up Flask, connects it to a SQLite database (`site.db`), and creates tables.

---

## 🏗️ Creating a Model

```python
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Profile {self.first_name} {self.last_name}>"
```

- `Column`: Creates a database column
- `primary_key`: Uniquely identifies each row
- `nullable`: Prevents empty fields

---

## 🖥️ Displaying Data on Index Page

Use `index.html` and Jinja2 templating to loop through profiles and show them in a table.

### Flask Route:
```python
@app.route('/')
def index():
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)
```

---

## 📝 Adding Data via Form

Create `add_profile.html` with a form to collect profile data.

### Route to render form:
```python
@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')
```

### Route to handle form submission:
```python
@app.route('/add', methods=["POST"])
def profile():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")

    if first_name and last_name and age:
        p = Profile(first_name=first_name, last_name=last_name, age=age)
        db.session.add(p)
        db.session.commit()
    return redirect('/')
```

---

## ❌ Deleting Records

### Deletion Route:
```python
@app.route('/delete/<int:id>')
def erase(id):
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
```

This function fetches a profile by ID, deletes it, and redirects to the index.

---

## 🧪 Run Your Application

```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000/add_data
```

Submit a profile form, return to home page, and see the updated list.

---

Flask-SQLAlchemy makes it easy to work with structured data using clean Python syntax and provides full CRUD functionality with minimal setup. 📦🧠
