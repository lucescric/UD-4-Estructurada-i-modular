from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 4. Presentar data del 10/12/2022 amb este format (exemple: '10 de desembre de 2022')
data_ex4 = date(2022, 12, 10)
# Nota: el nom del mes dependrà de la configuració de locale del sistema
print("4) Data 10/12/2022 amb format:", data_ex4.strftime("%d de %B de %Y"))
