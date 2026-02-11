from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 7. Comprovar si puc posar el dia 29 a 2/2020
try:
    data_ex7 = date(2020, 2, 29)
    print("7) El 29/2/2020 és una data vàlida:", True, "->", data_ex7)
except ValueError:
    print("7) El 29/2/2020 és una data vàlida:", False)
