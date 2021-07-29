entier_base_decimale = int(input("Veuillez entrer un nombre entier : "))

reste = 0
code = ""

while entier_base_decimale != 0:

    entier_base_decimale = entier_base_decimale // 2
    reste = entier_base_decimale % 2
    if reste == 0:
        code += "0" 
    else:
        code += "1"
    
print("L'équivalent binaire de votre nombre entier est : {}".format(code))

