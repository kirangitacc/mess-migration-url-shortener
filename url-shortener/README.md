# 🔗 URL Shortener API

A lightweight, thread-safe URL shortening service built with Flask. Supports shortening URLs, redirection, click tracking, and basic analytics — all using an in-memory store.

---

## 🚀 Features

- 🔗 Shorten valid URLs
- 🔁 Redirect using short codes
- 📈 Track click counts
- 📊 View analytics (clicks and creation time)
- 🧵 Thread-safe with `threading.Lock`
- ✅ Fully tested with `pytest`

---

## 🛠️ Tech Stack

- Python 3.13+
- Flask
- Pytest

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# (Optional) Create and activate a virtual environment
python -m venv venv
# On Windows
.env\Scriptsctivate
# On macOS/Linux
source venv/bin/activate

# Install Flask
pip install flask
```

---

## ▶️ Running the Server

Start the Flask development server using:

```bash
python -m flask --app app.main run
```

> Ensure your `app/main.py` file contains:
> ```python
> from flask import Flask
> app = Flask(__name__)
> ```

Server will be available at: [http://localhost:5000](http://localhost:5000)

---

## 📮 API Endpoints

### ✅ Health Check

```http
GET /
```

**Response:**

```json
{
  "status": "healthy",
  "service": "URL Shortener API"
}
```

---

### 🔗 Shorten URL

```http
POST /api/shorten
Content-Type: application/json
```

**Body:**

```json
{
  "url": "https://example.com"
}
```

**Response:**

```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

---

### 🔁 Redirect

```http
GET /<short_code>
```

**Response:**  
HTTP 302 redirect to the original URL.

---

### 📊 Analytics

```http
GET /api/stats/<short_code>
```

**Response:**

```json
{
  "url": "https://example.com",
  "clicks": 5,
  "created_at": "2025-08-04T10:44:03.497620Z"
}
```

---

## 🧪 Running Tests

```bash
python -m pytest -v
```

Unit tests are available in `tests/test_basic.py`.

---

## 📁 Project Structure

```
url-shortener/
├── app/
│   ├── main.py         # Flask app and routes
│   ├── models.py       # In-memory store and logic
│   └── utils.py        # URL validation
├── tests/
│   └── test_basic.py   # Pytest test cases
└── README.md
```

---

## 📌 Notes

- In-memory store: all data is lost when the server restarts.
- For production, use a persistent database.
- Thread safety is managed with `threading.Lock`.

---

## 🧠 Author

Built by **Kiran** — a persistent, detail-oriented full-stack developer focused on clean code, concurrency safety, and robust backend services.

---

## AI Usage

## 🤖 AI Usage Disclosure

This project was developed with assistance from Microsoft Copilot.

### Tools Used
- **Microsoft Copilot (Chat)**

### Purpose
- Helped design the project structure
- Provided complete code for Flask routes, thread-safe storage, and analytics
- Assisted in writing and refining test cases using `pytest`
- Generated the `README.md` and submission documentation

### Modifications
- All AI-generated code was reviewed, tested, and adapted to meet assignment requirements
- Manual adjustments were made to ensure correctness, clarity, and maintainability

AI was used as a productivity tool, similar to documentation, Stack Overflow, or IDE suggestions.


---

## 📜 License

MIT License
