import datetime 

dt = datetime.datetime.now()
d0 = datetime.date(dt.year, dt.month, dt.day)

print(d0)
t=datetime.date.today()
d1 = datetime.datetime(t.year, t.month, t.day)
print(d1)

print(datetime.datetime.min.time)
05/05/28