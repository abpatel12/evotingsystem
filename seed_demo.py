import secrets
import mysql.connector
from werkzeug.security import generate_password_hash
from config import Config

def main():
    if not Config.MYSQL_PASSWORD and Config.MYSQL_USER != "root":
        print("Check MYSQL_PASSWORD in .env before seeding.")
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST, port=Config.MYSQL_PORT, user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD, database=Config.MYSQL_DATABASE
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        if cur.fetchone()[0] > 0:
            print("Seed cancelled: users table is not empty. Avoid overwriting existing data.")
            return
        voter_hash = generate_password_hash("ChangeMe-Voter-2026!")
        admin_hash = generate_password_hash("ChangeMe-Admin-2026!")
        cur.execute("INSERT INTO users (username,password_hash,role,mfa_enabled) VALUES (%s,%s,'voter',FALSE)", ("voter1", voter_hash))
        voter_id = cur.lastrowid
        cur.execute("INSERT INTO users (username,password_hash,role,mfa_enabled) VALUES (%s,%s,'admin',FALSE)", ("admin1", admin_hash))
        cur.execute("INSERT INTO elections (title,description,status) VALUES (%s,%s,'open')", ("Student Council Election", "Synthetic election for the coursework prototype."))
        election_id = cur.lastrowid
        cur.executemany("INSERT INTO candidates (election_id,candidate_name) VALUES (%s,%s)", [
            (election_id, "Candidate A"), (election_id, "Candidate B"), (election_id, "Candidate C")
        ])
        cur.execute("INSERT INTO voter_eligibility (user_id,election_id,eligible) VALUES (%s,%s,TRUE)", (voter_id, election_id))
        conn.commit()
        print("Demo data created.")
        print("Voter: voter1 / ChangeMe-Voter-2026!")
        print("Admin: admin1 / ChangeMe-Admin-2026!")
        print("Election ID:", election_id)
        print("Change demo passwords before sharing the application.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
