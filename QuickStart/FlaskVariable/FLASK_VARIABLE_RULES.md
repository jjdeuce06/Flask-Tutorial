# Flask Variable Rules

Flask's variable rules allow developers to define **dynamic URLs** by embedding variables directly into route paths. This lets you capture values from the URL and pass them into view functions.

---

## 🌐 What Are Variable Rules?

A variable rule is defined using the syntax `<variable_name>` in a route. The captured value is passed as a **keyword argument** to the associated view function.

Example:
```python
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"
```

---

## 🔁 Benefits

- Enables dynamic content rendering
- Simplifies user-specific pages and filters
- Cleaner and more readable URLs

---

## 🧰 Available Converters in Flask

| Converter | Description                                 |
|-----------|---------------------------------------------|
| `string`  | Default. Accepts any text without slashes   |
| `int`     | Accepts only integer numbers                |
| `float`   | Accepts positive floating-point numbers     |
| `path`    | Like `string`, but allows slashes           |
| `any`     | Matches any one of the listed items         |
| `uuid`    | Accepts UUID strings                        |

---

## 🚀 Examples by Variable Type

### ✅ Basic Flask App

A simple welcome message app.  
📁 Code location: `FlaskVariable/app.py`  
▶️ Run with:
```bash
python app.py
```

---

### 🔤 String Variable in Flask

Defines a route that handles a string variable.

```python
@app.route('/vstring/<name>')
def greet(name):
    return f"Hello, {name}!"
```

📁 Code location: `FlaskVariable/string_test.py`  
▶️ Run with:
```bash
python string_test.py
```
🔗 Visit:
```
http://127.0.0.1:5000/vstring/YourName
```

---

### 🔢 Integer Variable in Flask

Handles a dynamic integer value.

```python
@app.route('/vint/<int:age>')
def show_age(age):
    return f"You are {age} years old."
```

📁 Code location: `FlaskVariable/int_test.py`  
▶️ Run with:
```bash
python int_test.py
```
🔗 Visit:
```
http://127.0.0.1:5000/vint/25
```

---

### 🌡️ Float Variable in Flask

Handles a dynamic floating-point number.

```python
@app.route('/vfloat/<float:accountbalance>')
def show_balance(accountbalance):
    return f"Your account balance is ${accountbalance}"
```

📁 Code location: `FlaskVariable/float_test.py`  
▶️ Run with:
```bash
python float_test.py
```
🔗 Visit:
```
http://127.0.0.1:5000/vfloat/1050.75
```

---

These dynamic routes make it easy to build user-personalized pages, input validators, and API endpoints using clean, intuitive URLs.

