
# 🧾 Flask-WTF Tutorial

Flask-WTF is a Flask extension that simplifies form handling using the powerful **WTForms** library. It helps manage form creation, validation, and rendering securely and efficiently.

---

## ✨ Key Features

- 🔒 **Secure Form Handling**: Built-in CSRF protection.
- 🎨 **Easy Form Rendering**: Supports multiple field types.
- ✅ **Built-in Validation**: Includes required checks, patterns, and custom validators.
- 📁 **File Uploads**: Allows uploading files through forms.

---

## ⚙️ Installation

```bash
pip install flask-WTF
```

In your Flask application:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
```

---

## 🧱 Common WTForms Field Types

| Field Type       | Description                               |
|------------------|-------------------------------------------|
| `StringField`    | Basic text input                          |
| `PasswordField`  | Input for passwords                       |
| `BooleanField`   | Checkbox (True/False)                     |
| `DecimalField`   | Input for decimal values                  |
| `RadioField`     | Radio buttons for single option selection |
| `SelectField`    | Dropdown list                             |
| `TextAreaField`  | Multiline text area                       |
| `FileField`      | File upload input                         |

---

## 🧪 Example 1 – Form with All Field Types

**Location:** `FirstExample/app.py`

### Components:

1. **Form Class** `MyForm`: Inherits from `FlaskForm` and includes multiple field types.
2. **HTML Template** `index.html`: Uses `{{ form.field_name.label }}` and `{{ form.field_name }}` to render the form.
3. **Validation**: `form.validate_on_submit()` handles POST and ensures all validations pass.
4. **Security**: Uses `generate_password_hash()` to encrypt passwords.

### Example Route:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # handle form data here
        return "Form submitted successfully"
    return render_template('index.html', form=form)
```

---

## 🧪 Example 2 – Simple Sign-up Form

**Location:** `SecondExample/app.py`

### HTML Template: `Signup.html`

```html
<form method="POST">
  {{ form.csrf_token }}
  {{ form.username.label }} {{ form.username }}
  {{ form.password.label }} {{ form.password }}
  {{ form.submit }}
</form>
```

### Explanation:

- `{{ form.csrf_token }}`: Adds CSRF protection.
- Fields like `username` and `password` are rendered using `label` and field variables.
- The form is only processed if submitted and valid.

### Flask Route:

```python
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return f"Welcome, {form.username.data}!"
    return render_template('signup.html', form=form)
```

---

## ✅ Summary

| Feature            | Benefit                          |
|--------------------|----------------------------------|
| CSRF Protection     | Security against malicious posts |
| Field Abstraction   | Clean, reusable Python classes   |
| Simple HTML Binding | Jinja integration                |
| Built-in Validators | Reliable form data handling      |

Flask-WTF helps create secure, clean, and interactive forms—perfect for login systems, registration, settings, and more! 🧩
