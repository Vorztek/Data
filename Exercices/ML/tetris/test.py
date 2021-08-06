import csv

list_1 = ["Hello", "World", "Monty", "Python"]
list_2 = [1, 2, 3, 4]


file = open(r"C:\Users\vion1\Ele\Engie\Exercices\ML\tetris\dataset.csv", "w")
writer = csv.writer(file)

for w in range(4):

  writer.writerow([list_1[w], list_2[w]])

file.close()