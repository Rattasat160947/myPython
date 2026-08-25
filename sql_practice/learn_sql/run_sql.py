import csv
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "practice.db"
CSV_PATH = BASE_DIR / "machine_results.csv"
DEFAULT_SQL_FILE = Path(__file__).resolve().parent / "basic.py"


def ensure_drive_test_table(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='drive_test'"
    )
    exists = cur.fetchone() is not None
    if exists:
        return

    cur.execute(
        """
        CREATE TABLE drive_test (
            serial TEXT PRIMARY KEY,
            machine TEXT NOT NULL,
            temperature REAL NOT NULL,
            result TEXT NOT NULL
        )
        """
    )

    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = [
            (row["serial"], row["machine"], float(row["temperature"]), row["result"])
            for row in reader
        ]

    cur.executemany(
        "INSERT INTO drive_test (serial, machine, temperature, result) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()


def run_sql_from_file(sql_file: Path) -> None:
    if not sql_file.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_file}")

    sql = sql_file.read_text(encoding="utf-8").strip()
    if not sql:
        raise ValueError("SQL file is empty")

    statements = [stmt.strip() for stmt in sql.split(";") if stmt.strip()]
    if not statements:
        raise ValueError("No SQL statements found")

    conn = sqlite3.connect(DB_PATH)
    try:
        ensure_drive_test_table(conn)
        cur = conn.cursor()
        for i, statement in enumerate(statements, start=1):
            print(f"\n=== Query {i} ===")
            print(statement)
            cur.execute(statement)

            if cur.description is not None:
                columns = [col[0] for col in cur.description]
                header = " | ".join(columns)
                print(header)
                print("-" * len(header))
                rows = cur.fetchall()
                if not rows:
                    print("(0 rows)")
                for row in rows:
                    print(" | ".join(str(value) for value in row))
            else:
                conn.commit()
                print(f"Done. Affected rows: {cur.rowcount}")
    finally:
        conn.close()


if __name__ == "__main__":
    sql_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_SQL_FILE
    run_sql_from_file(sql_path)
