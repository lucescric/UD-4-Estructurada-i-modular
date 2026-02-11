from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 8. Veure quina data és 30 dies després del 20/2/2010
data_inici_8 = date(2010, 2, 20)
data_mes_30 = data_inici_8 + timedelta(days=30)
print("8) 30 dies després del 20/2/2010 és:", data_mes_30)
