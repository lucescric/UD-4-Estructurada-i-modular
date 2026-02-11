from datetime import date, datetime, timedelta, time

# 11, 12, 13: entre 7/10/2001 i 10/5/2004
d1 = date(2001, 10, 7)
d2 = date(2004, 5, 10)

# mesos (complets)
anys_diff = d2.year - d1.year
mesos_diff = d2.month - d1.month
total_mesos = anys_diff * 12 + mesos_diff
if d2.day < d1.day:
    total_mesos -= 1
print("11. Mesos passats:", total_mesos)

# anys (complets)
anys_complets = d2.year - d1.year
if (d2.month, d2.day) < (d1.month, d1.day):
    anys_complets -= 1
print("12. Anys passats:", anys_complets)

# hores
dies_diff = (d2 - d1).days
hores_diff = dies_diff * 24
print("13. Hores passades:", hores_diff)
