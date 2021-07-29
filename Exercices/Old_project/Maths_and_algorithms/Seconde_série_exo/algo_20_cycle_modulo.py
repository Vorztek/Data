joueurs = ["Sarah", "Lucie", "Julien", "Eleonore"]

for i in range(100000):
    print("{}. Une carte est distribué à {}".format(i%4, joueurs[i%4])) 