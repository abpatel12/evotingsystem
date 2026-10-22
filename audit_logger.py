"""Audit logging helper for application events."""
import json

def log_audit(conn, event_type, actor_id=None, details=None):
    """Insert an audit event; never include candidate choice or raw voting tokens."""
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO audit_logs (actor_id, event_type, details) VALUES (%s, %s, %s)",
                    (actor_id, event_type, json.dumps(details or {})))
    finally:
        cur.close()
