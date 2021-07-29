def listAlphabet():
    alphabet = list(map(chr, range(97, 123)))
    return alphabet
    
def cryptage(cle, lettre):
    #lettre majuscule
    if 65 <= ord(lettre) <= 90: #On sait que c'est en majuscule
        return chr(65 + (ord(lettre) - 65 + cle) % 26 )

    #lettre minuscule
    elif 97 <= ord(lettre) <= 122: #On sait que c'est en majuscule
        return chr(97 + (ord(lettre) - 97 + cle) % 26 )

    else:
        return lettre


def cesar(cle, mot):
    texte = ""
    for i in mot:
        texte += cryptage(cle, i)
    return texte

print(cesar(10, "Je t'aime EleonoreEleonoreEleonoreEleonoreEleonoreEleonoreEleonore"))

