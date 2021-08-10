intervalle_début, intervalle_fin, pas = 0, 1000, 1

for j in range(1, 51):
    liste1 = []
    for i in range(intervalle_début, intervalle_fin, pas):
        liste1.append(i)
        print(liste1)

    intervalle_début += 1000
    intervalle_fin += 1000
    pas += 1

print(len(liste1))