"""Create a CSV export of vote records for local coursework backup demonstration."""
import csv
from datetime import datetime
from pathlib import Path
from app.db import get_connection
from app import create_app

def main():
    app = create_app()
    with app.app_context():
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT vote_id,election_id,candidate_id,integrity_tag,created_at FROM votes ORDER BY vote_id")
            rows = cur.fetchall()
            out = Path("backups")
            out.mkdir(exist_ok=True)
            path = out / f"votes-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["vote_id","election_id","candidate_id","integrity_tag","created_at"])
                writer.writerows(rows)
            print(f"Exported {len(rows)} vote records to {path}")
        finally:
            conn.close()

if __name__ == "__main__":
    main()
