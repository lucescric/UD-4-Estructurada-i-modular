from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar


# 3. Presentar data i hora en Europa/Madrid
ara_madrid = datetime.now(ZoneInfo("Europe/Madrid"))
print("3) Data i hora Europa/Madrid:", ara_madrid)
