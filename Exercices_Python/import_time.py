
values = []
def asking():
    keys = []
    
    for i in range(1, 22):
        keys.append(i)
        values = ["_"]
    #return keys #works fine here, keys is 1 to 21

    vide2 = dict(zip(keys, values))
    return vide2

print(asking())

fields = []

def bli():
    for i in range(1, 22):
        fields.append(i)
    return fields 

