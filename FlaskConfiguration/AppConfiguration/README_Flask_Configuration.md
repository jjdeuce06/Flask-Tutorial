
# ⚙️ Flask App Configuration Guide

Flask applications require configuration to manage important settings such as security, database connections, file uploads, and environment-specific behavior. This guide outlines best practices and examples for configuring your Flask app.

---

## 🔧 Setting Configurations with `app.config`

Flask uses a dictionary-like `app.config` to store configuration settings.

### Syntax:
```python
app.config['CONFIG_NAME'] = 'value'
```

- **CONFIG_NAME**: Built-in (like `DEBUG`, `SECRET_KEY`) or custom name.
- **value**: A string, boolean, integer, list, or dictionary.

---

## 🔐 Security Settings

### Secret Key
Used for sessions and CSRF protection:
```python
app.config['SECRET_KEY'] = 'your_secret_key'
```
Keep this key private. Use environment variables in production.

---

## 🛢️ Database Configuration

Flask supports SQLAlchemy for ORM and database access.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

For PostgreSQL:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
```

---

## 🧑‍💻 Session Management

Flask sessions can store user-specific data between requests.

```python
from datetime import timedelta

app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
```

- `SESSION_TYPE`: File-based session storage.
- `PERMANENT_SESSION_LIFETIME`: Duration before session expires.

---

## 🔄 JSON Response Settings

For Flask APIs, customize JSON behavior:

```python
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
```

- `JSON_SORT_KEYS`: Prevents automatic sorting of keys.
- `JSONIFY_PRETTYPRINT_REGULAR`: Beautifies JSON output.

---

## 📂 File Upload Configuration

To manage file uploads securely:

```python
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

- `UPLOAD_FOLDER`: Target directory for uploads.
- `MAX_CONTENT_LENGTH`: File size limit.

---

## 🗃️ Loading Config from External File

Create a `config.py` file:
```python
# config.py
SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
DEBUG = True
```

In `app.py`:
```python
app.config.from_pyfile('config.py')
```

---

## 🌍 Environment-Specific Configurations

Define different settings for `development`, `testing`, and `production`:

```python
if app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
```

### In `config.py`:
```python
class Config:
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod_db'
```

---

## 🐞 Enabling Debug Mode

During development:
```python
app.config['DEBUG'] = True
```
**Do NOT enable in production**. It exposes sensitive information and reloads automatically.

---

## ✅ Summary Table

| Configuration               | Key                          | Description                            |
|----------------------------|------------------------------|----------------------------------------|
| Secret Key                 | `SECRET_KEY`                 | Secures sessions and CSRF              |
| Database URI               | `SQLALCHEMY_DATABASE_URI`    | Connects to a database                 |
| Session Storage            | `SESSION_TYPE`               | Where to store session data            |
| Session Lifetime           | `PERMANENT_SESSION_LIFETIME` | Session expiry duration                |
| Upload Directory           | `UPLOAD_FOLDER`              | Where to save uploaded files           |
| Upload Limit               | `MAX_CONTENT_LENGTH`         | Maximum allowed upload size            |
| Debugging                  | `DEBUG`                      | Auto reload and error display          |
| JSON Output Style          | `JSONIFY_PRETTYPRINT_REGULAR`| Human-readable JSON                    |
| JSON Key Sorting           | `JSON_SORT_KEYS`             | Maintain insertion order               |

Flask's configuration system is flexible and scalable—perfect for small apps and production systems alike. 📦
