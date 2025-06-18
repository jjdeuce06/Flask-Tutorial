# Flask Web Development: First Simple Application

This project introduces the basics of building a web application using **Flask**, a lightweight and powerful web framework for Python. Flask, along with Django, is one of the most popular tools for developing web applications in Python.

---

## 🛠 Web Development with Python

There are several Python frameworks available for building web pages, such as:

- **Bottle**
- **Django**
- **Flask** (used in this project)

Among these, **Flask** and **Django** are the most popular due to their robust features and large communities.

---

## 📚 Key Concepts & Technologies

- **WSGI (Web Server Gateway Interface):**  
  A standard for communication between web servers and Python web applications.

- **Werkzeug:**  
  A WSGI toolkit used by Flask. It provides request and response objects, among other utilities.

- **Jinja2:**  
  A templating engine used in Flask to dynamically render HTML based on data.

- **Flask:**  
  A web application framework built on **Werkzeug** and **Jinja2**. All three are **Pocco projects**.

---

## ⚙️ Installation & Setup

### 1. Create a Virtual Environment
Using `virtualenv`, you can manage project-specific dependencies:

```bash
pip install virtualenv
virtualenv venv
```

### 2. Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source ./venv/bin/activate
  ```

> ⚠️ **Windows Users:**  
If you get an error saying the script cannot be loaded, open PowerShell **as Administrator** and run:

```powershell
Set-ExecutionPolicy RemoteSigned
```

Then try activating again.

### 3. Install Flask

```bash
pip install flask
```

---

## 🚀 Running Your First Flask Apps

### ✅ Hello World

Run your basic `HelloWorld.py` to test that Flask is working.

### ✅ Adding Variables

Next, try `AddingVariables.py` to see how Flask handles URL parameters and variables.

### ✅ Login Page

To try out the login functionality:

1. Run `LoginPage.py`
2. Open `login.html` in a browser
3. Submit the form and test the flow

---

## 📂 Project Structure Suggestion

```
project-root/
│
├── app.py
├── HelloWorld.py
├── AddingVariables.py
├── LoginPage.py
├── templates/
│   └── login.html
├── static/
│   └── (optional: CSS, JS files)
├── venv/
└── README.md
```

---

## 💡 Notes

- Flask keeps things minimal and extensible—you only add what you need.
- Great for small to medium web apps or APIs.
- Once you’re comfortable, you can add things like authentication, forms, databases, and deployment setups.

---

## 📬 Feedback

Feel free to fork the repo, open issues, or submit pull requests if you want to contribute or need help.

Happy coding! 🚀
