from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 6. Comprovar si l'any 2022 és bisiesto
any_ex6 = 2022
es_bisiest = calendar.isleap(any_ex6)
print(f"6) L'any {any_ex6} és bisiesto?:", es_bisiest)
