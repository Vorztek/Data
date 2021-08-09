def fibo_again(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a +b

print(fibo_again(200000000000000000000000000))

# a intergit avec n assez rapidement, ce qui bloque le programme, il faut plutôt utiliser un compteur