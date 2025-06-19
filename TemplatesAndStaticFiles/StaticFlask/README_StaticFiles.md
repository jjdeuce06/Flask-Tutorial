
# 🎵🎬 Static Files in Flask

Flask makes it easy to serve static files like CSS, JS, images, videos, and audio—all with zero server stress and maximum web joy.

## 📁 File Structure

Here’s a beautiful and totally not over-engineered directory layout:

![File Structure](static_files_structure.png)

_Yes, the image and media files are from Red Dead Redemption II. Why? Because cowboys need front-end frameworks too._ 🤠🎮

---

## 🧾 What Are Static Files?

**Static files** are things like:
- `CSS` stylesheets
- `JavaScript` scripts
- Media files (images, videos, audio)
- Fonts, PDFs, etc.

They don’t change unless you manually edit them (unlike dynamic content rendered by templates).

---

## 🧱 HTML Templates

HTML files go in the `templates/` folder. Example:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

Using Jinja, variables like `{{ message }}` can be rendered into these files.

---

## 🎨 Serving CSS

1. Place CSS in the `static/` folder.
2. Link it inside HTML:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## 📜 Serving JavaScript

1. Place JS in `static/`.
2. Link it similarly:

```html
<script src="{{ url_for('static', filename='serve.js') }}"></script>
```

---

## 🖼️🕹️🔊 Serving Media Files

Static folder also handles images, videos, and audio files.

### 1. Images

- HTML:
  ```html
  <img src="{{ url_for('static', filename='cat.jpg') }}" alt="Sample Image">
  ```
- Route in `main.py`:
  ```python
  @app.route("/image")
  def serve_image():
      message = "Image Route"
      return render_template('image.html', message=message)
  ```

### 2. Videos

- HTML:
  ```html
  <video controls>
    <source src="{{ url_for('static', filename='ocean_video.mp4') }}" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  ```
- Route in `main.py`:
  ```python
  @app.route("/video")
  def serve_video():
      message = "Video Route"
      return render_template('video.html', message=message)
  ```

### 3. Audio

- HTML:
  ```html
  <audio controls>
    <source src="{{ url_for('static', filename='audio.mp3') }}" type="audio/mp3">
    Your browser does not support the audio tag.
  </audio>
  ```
- Route in `main.py`:
  ```python
  @app.route("/audio")
  def serve_audio():
      message = "Audio Route"
      return render_template('audio.html', message=message)
  ```

---

## 🧪 Testing It

1. Run the Flask app with:
```
python main.py
```
2. Open the browser and navigate to:
- `http://127.0.0.1:5000/image`
- `http://127.0.0.1:5000/video`
- `http://127.0.0.1:5000/audio`

---

## 🙃 About That Cowboy Content...

> We deeply apologize for the wild west vibes. The static assets may have been rustled straight from Red Dead Redemption II, but hey—it loads fast and rides hard.

Yeehaw. 🐎
