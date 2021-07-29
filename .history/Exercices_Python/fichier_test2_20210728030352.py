class Person:
    def __init__(self, compte, valeur, compteur):
        self.compte = compte  #= 0
        self.valeur = valeur #= 300 #int(input("Veuillez saisir le nombre maximal de l'intervalle où seront cherchés les nombre premiers : "))
        self.compteur = compteur #= []

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe", "what")
x.printname()