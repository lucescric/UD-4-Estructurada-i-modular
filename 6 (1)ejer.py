from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+
import calendar

# 1. Presenta data actual
avui = date.today()
print("1) Data actual:", avui)  # format ISO: YYYY-MM-DD
