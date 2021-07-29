course_total = 7000

temps = 60
vitesse1 = 15000


course1 = 5000
temps1 = temps / (vitesse1/course1)

vitesse2 = 12000
course2 = course_total - course1
temps2 = temps / (vitesse2/course2)

temps_total = temps1 + temps2
print(temps_total)

#Le reste c'est chaud