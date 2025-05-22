from datetime import datetime, timedelta

# In-memory list of recent confirmed strikes
STRIKE_HISTORY = []

def get_confirmed_strikes(within_minutes=3):
    """Returns all confirmed strikes within the last `within_minutes`."""
    now = datetime.utcnow()
    return [
        strike for strike in STRIKE_HISTORY
        if "confirmed_time" in strike
        and (now - strike["confirmed_time"]) <= timedelta(minutes=within_minutes)
    ]

def add_strike(strike):
    """Adds a confirmed strike to memory history."""
    strike["confirmed_time"] = datetime.utcnow()
    STRIKE_HISTORY.append(strike)