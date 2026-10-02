from pathlib import Path
import sqlite3

root = Path(__file__).resolve().parent
data_dir = root / "data"
download_dir = data_dir / "downloads"
data_dir.mkdir(exist_ok=True)
download_dir.mkdir(exist_ok=True)

db_path = data_dir / "demo.db"
if db_path.exists():
    db_path.unlink()

conn = sqlite3.connect(db_path)
conn.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    role TEXT NOT NULL
)
""")
conn.executemany(
    "INSERT INTO users(username, role) VALUES (?, ?)",
    [("alice", "developer"), ("bob", "reviewer"), ("admin", "admin")],
)
conn.commit()
conn.close()

(download_dir / "public.txt").write_text(
    "Public demo file for FIXORA validation.\n", encoding="utf-8"
)

(root / "secrets" / "demo_secret.txt").write_text(
    "DEMO_SECRET=THIS_IS_NOT_A_REAL_CREDENTIAL\n", encoding="utf-8"
)

print(f"Demo database created at: {db_path}")
