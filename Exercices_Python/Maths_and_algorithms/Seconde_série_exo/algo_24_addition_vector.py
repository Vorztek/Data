vector1 = [1, 2, 3]
vector2 = [4, 5, 6]


def sum_vector():
    if len(vector1) != len(vector2):
        return None

    vector_somme = []
    for i in range(len(vector1)):
        vector_somme.append(vector1[i] + vector2[i])
    return vector_somme

print(sum_vector())

#ou methode zip
