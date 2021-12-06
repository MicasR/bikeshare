from datetime import datetime


def str_is_date(date_string: str, format: str = "%Y-%m-%d") -> bool:
    """Receive str return true if date, else return false."""
    if type(date_string) != str: return False
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

