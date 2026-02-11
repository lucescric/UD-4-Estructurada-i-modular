from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 10. Calcular quants dies han passat entre el 7/10/2001 i el 10/5/2004
data1_10 = date(2001, 10, 7)
data2_10 = date(2004, 5, 10)
dies_diferencia = (data2_10 - data1_10).days
print("10) Dies entre 7/10/2001 i 10/5/2004:", dies_diferencia)
