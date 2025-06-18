# Running a Flask Application

After creating a Flask app, you can run it on the development server using the **Flask CLI** or by executing the Python script directly.

## 🏃 Run Commands

Use either of the following commands in your terminal:

```bash
flask --app app_name run
```

or

```bash
python app_name.py
```

> Try both methods with the provided example: `app.py`

---

## 🗂️ File Structure Example

Here is an example Flask project file structure:

![Flask Project Structure](Screenshot%202025-06-17%20151304.png)

---

## 🐞 Debugging

With debug mode enabled, Flask automatically detects code changes and displays detailed error tracebacks. This helps developers quickly locate and fix issues.

Use the following block to enable debug mode:

```python
if __name__ == '__main__':  
    app.run(debug=True)
```

This ensures that your app runs with debugging features turned on during development.
