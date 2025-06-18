# Common HTTP Methods in Flask

Flask supports multiple HTTP methods, but the most commonly used are **GET** and **POST**. These methods define how data is sent between the browser (client) and your server (Flask app).

---

## 🔍 GET Method

The **GET** method is used to **request data from the server**. It's ideal for retrieving information without changing anything on the server.

### Key Characteristics

- Appends data to the URL as name-value pairs (`?key=value`)
- Easy to bookmark and share
- Cached by the browser
- **Not suitable for sensitive data** (URLs are logged and stored in history)

### ✅ Example Use Case

You created a square root calculator in the `GETExample` folder.

### ▶️ How to Run

1. Run the app:
   ```bash
   python app.py
   ```
2. Open your browser and go to the address shown (usually `http://127.0.0.1:5000`)
3. Append `/square` to the URL:
   ```
   http://127.0.0.1:5000/square
   ```

You’ll see a form where you can input a number, and it will show the square of that number using a GET request.

---

## 📨 POST Method

The **POST** method is used to **send data to the server**, usually when submitting forms or uploading files.

### Key Characteristics

- Sends data in the request body (not the URL)
- **More secure** for sensitive or long data
- Cannot be bookmarked
- Not cached by default

### ✅ Example Use Case

You modified the GET-based app in a new folder called `POSTExample`.

### ▶️ How to Run

1. Run the app:
   ```bash
   python app.py
   ```
2. Visit the app in your browser (e.g. `http://127.0.0.1:5000`)
3. Fill out the form and submit it

The data is sent via POST and processed by the server, which renders a result page with the output.

---

## 🔁 Summary Table

| Feature        | GET                          | POST                         |
|----------------|-------------------------------|-------------------------------|
| Data location  | URL                          | Request body                  |
| Bookmarkable   | Yes                          | No                            |
| Caching        | Yes                          | No                            |
| Use Case       | Fetching data                | Submitting forms              |
| Security       | Low (data visible in URL)    | High (data hidden in body)    |

---

## 🧪 Tip for Forms in Flask

When designing your form, use the appropriate method:

```html
<!-- For GET -->
<form method="GET" action="/square">
```

```html
<!-- For POST -->
<form method="POST" action="/square">
```

> Don’t forget to handle the method in your route:
```python
@app.route('/square', methods=['GET', 'POST'])
```

---

This foundation prepares you for working with user input, APIs, login systems, and more in Flask.

