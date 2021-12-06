from datetime import datetime


def str_is_date(date_string: str, format: str = "%Y-%m-%d") -> bool:
    """Check if str is in the correct date format"""
    if type(date_string) != str: return False
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False


def is_positive_float(item: str) -> bool:
    """Check if item is a positive float."""
    try:
        if float(item) <  0: return False
        if float(item) >= 0: return True
    except:
        return False
