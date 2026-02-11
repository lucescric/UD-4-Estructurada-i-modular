from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar

# 9. Veure quina data és 1 mes després del 15/12/2009
data_inici_9 = date(2009, 12, 15)
any9 = data_inici_9.year
mes9 = data_inici_9.month
dia9 = data_inici_9.day

# Sumar 1 mes manualment (sense llibreries extra)
nou_mes = mes9 + 1
nou_any = any9
if nou_mes > 12:
    nou_mes = 1
    nou_any += 1

# Ajustar el dia si el nou mes no té tants dies (per seguretat)
ultim_dia_nou_mes = calendar.monthrange(nou_any, nou_mes)[1]
nou_dia = min(dia9, ultim_dia_nou_mes)

data_mes_1 = date(nou_any, nou_mes, nou_dia)
print("9) 1 mes després del 15/12/2009 és:", data_mes_1)
