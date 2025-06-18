# Flask Redirects and Error Handling

Flask allows developers to **redirect users** to different URLs and manage HTTP errors gracefully using built-in utilities like `redirect()` and `abort()`.

---

## 🔀 Redirects in Flask

Redirects send the user to another URL along with a status code.

### 🔧 Syntax

```python
from flask import redirect

redirect(location, code=302)
```

#### Parameters:
- `location (str)`: URL to redirect to
- `code (int)`: HTTP status code (default is `302` — temporary redirect)

---

## ⚠️ Reasons for Errors

Web applications can produce errors due to:

- Unauthorized access or malformed requests
- Unsupported file types (media, uploads)
- Server overload or backend crash
- Internal hardware or connection issues

---

## 📑 Common HTTP Redirect and Error Codes

| Code | Description             |
|------|-------------------------|
| 300  | Multiple Choices        |
| 301  | Moved Permanently       |
| 302  | Found (Temporary)       |
| 303  | See Other               |
| 304  | Not Modified            |
| 305  | Use Proxy               |
| 306  | Reserved                |
| 307  | Temporary Redirect      |
| 400  | Bad Request             |
| 401  | Unauthenticated         |
| 403  | Forbidden               |
| 404  | Not Found               |
| 406  | Not Acceptable          |
| 415  | Unsupported Media Type  |
| 429  | Too Many Requests       |

---

## 🚀 Example: Redirect App

A simple redirect example using:

- `app.py` in `RedirectError` folder
- `login.html` in the `templates/` folder

### ▶️ How to Run

```bash
python app.py
```

Visit `http://127.0.0.1:5000` and you’ll be redirected to another route using `redirect()`.

---

## ❌ Error Handling with `abort()`

Flask's `abort()` function allows you to return an error response if something goes wrong.

### 🔧 Syntax

```python
from flask import abort

abort(code, message=None)
```

#### Example:

```python
@app.route('/user/<username>')
def check_username(username):
    if username[0].isdigit():
        abort(400, description="Username cannot start with a number.")
    return "Good username"
```

---

## 📄 Example: Abort Demo

📁 Code location: `RedirectError/abort_test.py`

### ▶️ How to Run

```bash
python abort_test.py
```

### 🧪 How to Test

1. Visit:
   ```
   http://127.0.0.1:5000/your_username
   ```
2. Try a username that starts with a number → triggers a `400 Bad Request`
3. Modify the code to:
   ```python
   abort(403)
   ```
   and re-test to see a `403 Forbidden` page.

---

Flask makes handling redirects and errors simple and customizable, giving you full control over how users are navigated or notified in your application.

