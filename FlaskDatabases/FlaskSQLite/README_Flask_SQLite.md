
# 🗄️ Flask with SQLite – Basic Web App Guide

Flask is a lightweight Python web framework that's easy to use for small to mid-sized projects. When paired with **SQLite**, it becomes a great solution for quickly storing and retrieving structured data.

---

## ⚙️ Installation

Run the following commands to get started:

```bash
pip install flask
pip install db-sqlite3
```

---

## 📁 File Structure

Once completed, your project should look like this:

![File Structure](flask_sqlite_structure.png)

---

## 📃 HTML Templates Overview

### `index.html`

- Has two buttons: one to display all participants and one to create a new entry.
- Note: VS Code may require splitting JavaScript from inline tags — restructure as needed.

### `join.html`

- A form that collects:
  - Name
  - Email
  - City
  - Country
  - Phone
- Uses `POST` method to send data to the server.
- Server stores this data in the SQLite database.

### `participants.html`

- Displays data in a table format.
- Uses `<th>` tags for headers and Jinja `{% for %}` loops to render rows.
- Each row is created with `<tr>` and each data field with `<td>`.

---

## 🐍 Python Logic in `app.py`

1. Set up Flask and SQLite.
2. Connect to the database using:
   ```python
   sqlite3.connect("database.db")
   ```
3. Create the table (if it doesn't exist) with fields:
   - Name
   - Email
   - City
   - Country
   - Phone

4. Use `render_template()` to serve HTML pages.
5. On form submission (`POST`), insert data into the database and commit the transaction.
6. Use a function to fetch all participants and display them via Jinja in `participants.html`.

### Sample Code to Fetch Participants:

```python
@app.route('/participants')
def participants():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM participants")
    data = cursor.fetchall()
    conn.close()
    return render_template('participants.html', participants=data)
```

---

## 🚀 How to Run the App

1. Activate your virtual environment.
2. Run your app with:
```bash
python app.py
```
3. Navigate to:
```
http://127.0.0.1:5000/
```

Try adding new participants and viewing the full list. The database (`database.db`) will automatically update with each new entry.

---

Flask + SQLite makes for a compact and effective stack for simple CRUD applications. 🧩🧠
