"""Compatibility exports for result integrity checks."""
from app.security import make_result_hash, verify_result_hash
__all__ = ["make_result_hash", "verify_result_hash"]
