# Flask App Routing

App Routing in Flask means mapping URLs to specific functions that handle the logic for those URLs. Modern web frameworks like Flask use **meaningful URLs** to improve user experience and site navigation.

---

## 🌐 Example Route

In our application, the URL `"/"` is associated with the root. To route something like `www.example.org/hello`, you define:

```python
@app.route('/hello')
def hello():
    return "Hello, World!"
```

> ✅ See code in `main.py`  
> The `hello` function is now mapped with the `/hello` path and will display its output in the browser.

---

## ▶️ Steps to Run

1. Run the application with:
   ```bash
   python app_name.py
   ```
2. Open your browser and visit:
   ```
   http://127.0.0.1:5000/hello
   ```

---

## 🔁 Dynamic URLs

You can also build dynamic URLs by using variables:

```python
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"
```

### 💡 Converters

You can convert variables using this syntax: `<converter:variable_name>`

| Converter | Description                              |
|-----------|------------------------------------------|
| `string`  | (default) accepts any text (no slashes)  |
| `int`     | accepts positive integers                |
| `float`   | accepts positive floating-point values   |
| `path`    | like string but accepts slashes too      |
| `uuid`    | accepts UUID strings                     |

> ✅ See full example in `convertercode.py`  
> Run with: `python convertercode.py` and follow on-screen instructions.

---

## 🛠️ Using `add_url_rule()`

Instead of `@app.route`, you can also map URLs using `add_url_rule()`:

```python
app.add_url_rule('/hello', 'hello', hello_function)
```

- `<url rule>`: the route path
- `<endpoint>`: optional internal identifier
- `<view function>`: the function to execute

> ✅ See example in `URLFunction.py`  
> Run with: `python URLFunction.py` and follow home screen instructions.

---

This gives you flexible routing control and helps when importing view functions from other modules.
