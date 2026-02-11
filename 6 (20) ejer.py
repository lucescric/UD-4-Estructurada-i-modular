from datetime import date, datetime, timedelta, time

# 20: data corresponent al dia 253 de 1989
d20 = date(1989, 1, 1) + timedelta(days=252)  # 252 perquè el dia 1 és el 0
print("20. Dia 253 de 1989:", d20.strftime("%d/%m/%Y"))
