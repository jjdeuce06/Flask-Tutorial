# Changing the Port in a Flask App

By default, Flask runs your application on port **5000**. You can access it via:

```
http://127.0.0.1:5000/
```

However, you may want to change the port number if:
- Port 5000 is already in use
- You're running multiple Flask apps simultaneously
- You want to match production or deployment environments

---

## 🔧 How to Change the Port

You can specify the port when calling `app.run()` in your `if __name__ == '__main__'` block:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

Replace `8000` with any other port number you prefer.

---

## ▶️ Example

This example returns plain text when hitting the root URL `/`.

📁 Code location: `helloworld.py`

### ▶️ How to Run

```bash
python helloworld.py
```

Then visit:

```
http://127.0.0.1:8000/
```

You should see your message rendered from the root route.

---

Changing the port is helpful when you're working with multiple local servers or facing port conflicts.
