
# 📁 Handling File Uploads in Flask

Uploading files in Flask is a common task—whether it’s profile pictures, documents, or homework. Flask makes this process straightforward and flexible.

---

## 🗂️ Example Project Structure

Here's how your file structure might look:

![File Upload Structure](file_upload_structure.png)

---

## 📥 How File Upload Works in Flask

- HTML forms must have `enctype="multipart/form-data"`.
- Files are sent via the `request.files` object.
- Flask can save files anywhere using `.save()`.

---

## ⚙️ Installation

Make sure Flask is installed:

```bash
pip install flask
```

---

## 🧪 Step-by-Step Implementation

### Step 1: Project Setup

Create a folder named `FileUpload` (or similar), and inside it:
- `templates/` (for HTML files)
- `main.py` (your Flask app)

### Step 2: HTML Upload Form (`index.html`)

Inside `templates/index.html`:
```html
<form method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
```

### Step 3: Upload Acknowledgement Page (`Acknowledgement.html`)

```html
<h2>File uploaded successfully!</h2>
<p>Your file has been received by the server.</p>
```

### Step 4: Flask Server (`main.py`)

```python
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(os.getcwd(), f.filename))
        return render_template('Acknowledgement.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🚀 Running the App

Run this command in your terminal:
```
python main.py
```

Open your browser and go to `http://127.0.0.1:5000/` to see the upload form.

---

## ✅ Result

Once the file is uploaded:
- You’ll see the **Acknowledgement** page.
- The uploaded file will appear in the same folder as `main.py`.

Now you have a working file upload system using Flask! 🎉
