"""Compatibility exports for demo login throttling."""
from app.security import login_rate_limited, record_failed_login, clear_failed_logins
__all__ = ["login_rate_limited", "record_failed_login", "clear_failed_logins"]
