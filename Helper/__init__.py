from datetime import datetime

from dateutil import tz


def convert_utc_rome(utc_time: datetime):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/Rome')
    utc = utc_time.replace(tzinfo=from_zone)
    rome_time = utc.astimezone(to_zone)
    return rome_time
