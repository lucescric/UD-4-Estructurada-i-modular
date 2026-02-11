from datetime import date, datetime, timedelta, time

# 14: període entre 3/2/2020 i 5/7/2021
p1 = date(2020, 2, 3)
p2 = date(2021, 7, 5)

anys = p2.year - p1.year
mesos = p2.month - p1.month
dies = p2.day - p1.day

if dies < 0:
    mesos -= 1
    # agafem el mes anterior a p2
    if p2.month == 1:
        mes_anterior = 12
        any_anterior = p2.year - 1
    else:
        mes_anterior = p2.month - 1
        any_anterior = p2.year
    # últim dia del mes anterior
    ultim_dia_mes_anterior = (
        (date(any_anterior, mes_anterior + 1, 1) - timedelta(days=1)).day
        if mes_anterior != 12
        else 31
    )
    dies += ultim_dia_mes_anterior

if mesos < 0:
    anys -= 1
    mesos += 12

print(f"14. Període: {anys} anys, {mesos} mesos i {dies} dies")
