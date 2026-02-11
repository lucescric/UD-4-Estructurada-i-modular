from datetime import date, datetime, timedelta, time

# 15: sumar aquest període a 12/11/2022
base = date(2022, 11, 12)
any_nou = base.year + anys
mes_nou = base.month + mesos
if mes_nou > 12:
    any_nou += (mes_nou - 1) // 12
    mes_nou = ((mes_nou - 1) % 12) + 1

# ajust de dies
try:
    data_temp = date(any_nou, mes_nou, base.day)
except ValueError:
    # si el dia no existix (p.ex. 31 de febrer), posem l'últim del mes
    if mes_nou == 12:
        data_temp = date(any_nou, mes_nou, 31)
    else:
        data_temp = date(any_nou, mes_nou + 1, 1) - timedelta(days=1)

data_final = data_temp + timedelta(days=dies)
print("15. Data resultant:", data_final.strftime("%d/%m/%Y"))
