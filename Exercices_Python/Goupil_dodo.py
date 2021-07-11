import datetime

film_name = input("What is the movie name ?")

Date = input("When it's up ?")
date_format = "%d/%m/%y"

d1 = datetime.datetime.strptime(Date, date_format)
d0 = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())

d2 = (d1 - d0).days

print("Il reste {} dodos avant la sortie de {}".format(d2, film_name))