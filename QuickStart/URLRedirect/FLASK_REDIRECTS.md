# Flask Redirects and URL Handling

Flask is a lightweight Python web framework used to build backend applications quickly and efficiently. It supports URL routing, redirecting, and response handling — core features for any web application.

---

## 🔀 What is a Redirect?

A **redirect** sends the user from one URL to another. It's commonly used after form submissions, login workflows, or when redirecting users to another part of the app.

### 🔧 Syntax

```python
from flask import redirect

redirect(location, code=302)
```

#### Parameters:
- `location (str)`: The target URL or endpoint.
- `code (int)`: HTTP status code (default is `302` for a temporary redirect).

### 🔁 Return:
A redirect response object that sends the user to a new URL.

---

## 📑 Common HTTP Redirect Codes

| Code | Description             |
|------|-------------------------|
| 300  | Multiple Choices        |
| 301  | Moved Permanently       |
| 302  | Found (default redirect)|
| 303  | See Other               |
| 304  | Not Modified            |
| 305  | Use Proxy               |
| 306  | Reserved                |
| 307  | Temporary Redirect      |

---

## 🚀 Example: Redirect on Base Route

This example has two routes:

- `/` → redirects to `/helloworld`
- `/helloworld` → displays a message

📁 Code location: `URLRedirect/app.py`  
▶️ Run with:

```bash
python app.py
```

After starting, visit:
```
http://127.0.0.1:5000/
```

You’ll automatically be redirected to:
```
http://127.0.0.1:5000/helloworld
```

---

## 🔗 `url_for()` Function in Flask

Flask also includes a utility function called `url_for()` to build dynamic URLs based on **function names**, not hard-coded paths.

### Example Behavior

A function named `user(name)`:
- If `name == 'admin'`, it redirects to `hello_admin()`
- Otherwise, it redirects to `hello_guest()`

### ✅ Benefits of `url_for()`

- Avoids hardcoding URLs
- Easier to refactor
- More readable and maintainable

📁 Code location: `URLRedirect/url_test.py`  
▶️ Run with:

```bash
python url_test.py
```

Then click the links shown in the browser:
- For admin: will redirect to admin page
- For guest: change the `guest` name in the URL to your own

---

This gives you a powerful way to manage user flows and dynamic routing in your Flask applications.
