from datetime import datetime

PRIORITIES = ["Low", "Medium", "High"]
CATEGORIES = ["Work", "Personal", "Study", "Other"]

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
