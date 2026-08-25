import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "machine_results.csv"
DB_PATH = BASE_DIR / "practice.db"


def load_csv_to_sqlite() -> None:
    """Load CSV rows into SQLite table for SQL practice."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS machine_results")
    cur.execute(
        """
        CREATE TABLE machine_results (
            serial TEXT PRIMARY KEY,
            machine TEXT NOT NULL,
            temperature REAL NOT NULL,
            result TEXT NOT NULL
        )
        """
    )

    with CSV_PATH.open("r", encoding="utf-8") as f:
        rows = [line.strip().split(",") for line in f.readlines()[1:] if line.strip()]

    cur.executemany(
        "INSERT INTO machine_results (serial, machine, temperature, result) VALUES (?, ?, ?, ?)",
        [(s, m, float(t), r) for s, m, t, r in rows],
    )

    conn.commit()
    conn.close()


def run_demo_queries() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    queries = [
        ("All rows", "SELECT * FROM machine_results"),
        ("Only FAIL", "SELECT serial, machine, temperature FROM machine_results WHERE result = 'FAIL'"),
        (
            "Average temperature by machine",
            "SELECT machine, ROUND(AVG(temperature), 2) AS avg_temp FROM machine_results GROUP BY machine",
        ),
        (
            "Fail count by machine",
            "SELECT machine, COUNT(*) AS fail_count FROM machine_results WHERE result = 'FAIL' GROUP BY machine",
        ),
    ]

    for title, sql in queries:
        print(f"\n--- {title} ---")
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)

    conn.close()


if __name__ == "__main__":
    load_csv_to_sqlite()
    run_demo_queries()
