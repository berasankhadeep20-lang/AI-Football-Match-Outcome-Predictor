from datetime import datetime

def get_current_season():

    today = datetime.today()

    year = today.year
    month = today.month

    # European football seasons start around August
    if month >= 8:
        return year
    else:
        return year - 1