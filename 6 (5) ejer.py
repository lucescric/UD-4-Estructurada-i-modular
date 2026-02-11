from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 5. Indicar a quin mes correspon el 7/12/2020, en número i el nom
data_ex5 = date(2020, 12, 7)
mes_num = data_ex5.month
mes_nom = data_ex5.strftime("%B")
print(f"5) Mes del 7/12/2020: número {mes_num}, nom {mes_nom}")
