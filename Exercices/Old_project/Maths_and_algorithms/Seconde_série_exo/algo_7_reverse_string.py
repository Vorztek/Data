# Methode join

def reverse_join(string):
    string = ",".join(reversed(string))
    return string

print(reverse_join("Eleonore"))

#Autre python

print("Eleonore"[::-1])