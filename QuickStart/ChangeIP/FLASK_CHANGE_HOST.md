# Changing Host IP Address in Flask

By default, Flask runs on:

```
http://127.0.0.1:5000
```

This means the app can **only be accessed from the same machine**.

---

## 🌐 Why Change the Host?

If you want to access your Flask app from:

- Another device on the same Wi-Fi/network
- A mobile device
- The public internet (via port forwarding or tunneling)

…you must **change the host IP** to make the app publicly accessible.

---

## 🧪 How to Change the Host in Code

Modify the `app.run()` call in `app.py`:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

- `host='0.0.0.0'` → makes it accessible on all network interfaces
- `port=5000` → (or any other port you prefer)

📁 Code location: `app.py`

### ▶️ How to Run

```bash
python app.py
```

Then access the app on another device by replacing `127.0.0.1` with your **local IP address** (e.g., `192.168.1.50:5000`)

---

## ⚙️ Setting Host via Command Line

You can also set the host and port without modifying code.

### 🧾 Steps

1. Set the Flask app environment variable:

```bash
# Windows
set FLASK_APP=app.py

# Linux/macOS
export FLASK_APP=app.py
```

2. Run Flask with a custom host and port:

```bash
flask run --host=0.0.0.0 --port=5000
```

Now your app is visible to devices on the same network.

> 💡 Use `ipconfig` (Windows) or `ifconfig` / `ip a` (Linux/macOS) to find your device’s local IP address.

---

**Caution:** Exposing apps to the internet requires proper security (authentication, firewalls, HTTPS, etc.)

