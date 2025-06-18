# Flask Models & ORM Integration

In Flask, **models** represent your application's data structure and handle interactions with the database. Instead of writing raw SQL queries, models allow developers to interact using Python classes, making database operations easier and more efficient.

---

## 📦 What is ORM in Flask?

**ORM (Object Relational Mapping)** allows you to map Python classes to database tables. Flask doesn't include built-in ORM support, but the `Flask-SQLAlchemy` extension adds this capability.

> ✅ Most commonly used ORM in Flask is **SQLAlchemy**

---

## 📄 Declaring Models in Flask

### Step 1: Install Flask-SQLAlchemy

```bash
pip install flask-sqlalchemy
```

### Step 2: Import Modules

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
```

### Step 3: Configure Flask App and Database

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

- `SQLALCHEMY_DATABASE_URI`: Path to the SQLite database
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Disabled for performance

### Step 4: Initialize the Database

```python
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
```

### Step 5: Define a Model

```python
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    event = db.Column(db.String(200), nullable=False)
```

- `id`: Auto-increment primary key
- `date`: Timestamp of the event
- `event`: Event description

### Step 6: Create the Database Tables

```python
with app.app_context():
    db.create_all()
```

> Converts your models into actual tables in the database.

---

## 📝 Adding and Querying Data

### Add Event

```python
def add_event(event_description):
    new_event = Event(event=event_description)
    db.session.add(new_event)
    db.session.commit()
```

### Query Events

```python
events = db.session.execute(db.select(Event).order_by(Event.date)).scalars()
```

Access in template:
- `e.date` → Event date
- `e.event` → Event description

---

## 🧪 Flask App Using Models

Build a simple app `eventLog` that lets you add and view events. The date and time are added automatically.

### 📁 File Structure

```
FirstFlaskAppModel/
│
├── eventLog/
│   ├── templates/
│   │   └── home.html
│   └── app.py
```

---

## 🧵 Description of `app.py`

- Uses SQLite to manage events
- Contains `create_app()` factory to set up the app
- Defines `Event` model using SQLAlchemy
- Adds a route to display and add events
- Includes `init-db` CLI command to initialize the database

---

## ▶️ How to Run

In your terminal:

```bash
venv\Scripts\activate     # activate virtual environment (Windows)
flask init-db               # initialize the database
python app.py               # run the Flask app
```

> You can then access the app and use the form on the home page to add new events dynamically.

---

This approach provides clean, maintainable, and scalable code for any Flask app that uses databases.

