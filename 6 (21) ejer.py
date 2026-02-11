from datetime import date, datetime, timedelta, time

# 21: segons entre 10.15 i 12.30
t1 = time(10, 15)
t2 = time(12, 30)
dt1 = datetime.combine(date.today(), t1)
dt2 = datetime.combine(date.today(), t2)
segons = int((dt2 - dt1).total_seconds())
print("21. Segons entre 10.15 i 12.30:", segons)
