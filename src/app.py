from flask import Flask, request, Response
import hashlib
import os
import sqlite3

app = Flask(__name__)

DEMO_API_KEY = "DEMO_ONLY_NOT_A_REAL_SECRET_12345"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "demo.db")
DOWNLOAD_DIR = os.path.join(BASE_DIR, "data", "downloads")


def get_db():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def index():
    return {
        "project": "FIXORA Demo Project",
        "warning": "Intentionally vulnerable. Local demo only."
    }


@app.get("/user")
def user_lookup():
    # Intentionally vulnerable: SQL Injection (CWE-89)
    name = request.args.get("name", "")
    query = f"SELECT id, username, role FROM users WHERE username = '{name}'"
    conn = get_db()
    rows = conn.execute(query).fetchall()
    conn.close()
    return {"query": query, "rows": rows}


@app.get("/download")
def download():
    # Intentionally vulnerable: Path Traversal (CWE-22)
    filename = request.args.get("file", "public.txt")
    path = os.path.join(DOWNLOAD_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return Response(f.read(), mimetype="text/plain")


@app.get("/hello")
def hello():
    # Intentionally vulnerable: reflected HTML / XSS-style output (CWE-79)
    name = request.args.get("name", "developer")
    return Response("<h1>Hello " + name + "</h1>", mimetype="text/html")


@app.get("/hash")
def weak_hash():
    # Intentionally weak cryptographic hash (CWE-328)
    value = request.args.get("value", "")
    digest = hashlib.md5(value.encode("utf-8")).hexdigest()
    return {"md5": digest}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
