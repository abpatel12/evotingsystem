"""Basic health-check helper for monitoring scripts."""
def service_status():
    """Return a minimal status payload without exposing secrets."""
    return {"status": "ok", "service": "electronic-voting-prototype"}
