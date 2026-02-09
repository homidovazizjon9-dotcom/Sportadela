import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "stats.json"
DB_PATH = BASE_DIR / "stats.db"

with DATA_PATH.open("r", encoding="utf-8") as f:
    payload = json.load(f)

if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE metadata (
        id INTEGER PRIMARY KEY,
        source TEXT NOT NULL,
        as_of TEXT NOT NULL
    )
    """
)
cur.execute(
    """
    CREATE TABLE standings (
        position INTEGER,
        team TEXT,
        played INTEGER,
        wins INTEGER,
        draws INTEGER,
        losses INTEGER,
        goals_for INTEGER,
        goals_against INTEGER,
        points INTEGER,
        form TEXT
    )
    """
)
cur.execute(
    """
    CREATE TABLE fixtures (
        date TEXT,
        time TEXT,
        home TEXT,
        away TEXT,
        venue TEXT,
        status TEXT
    )
    """
)

cur.execute(
    "INSERT INTO metadata (source, as_of) VALUES (?, ?)",
    (payload["source"], payload["as_of"]),
)

cur.executemany(
    """
    INSERT INTO standings (
        position, team, played, wins, draws, losses, goals_for, goals_against, points, form
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    [
        (
            row["position"],
            row["team"],
            row["played"],
            row["wins"],
            row["draws"],
            row["losses"],
            row["goals_for"],
            row["goals_against"],
            row["points"],
            row["form"],
        )
        for row in payload["standings"]
    ],
)

cur.executemany(
    """
    INSERT INTO fixtures (date, time, home, away, venue, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    [
        (
            row["date"],
            row["time"],
            row["home"],
            row["away"],
            row["venue"],
            row["status"],
        )
        for row in payload["fixtures"]
    ],
)

conn.commit()
conn.close()
