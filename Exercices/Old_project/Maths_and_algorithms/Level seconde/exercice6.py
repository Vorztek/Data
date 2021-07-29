
def f():
    x = int(input("Donnez une valeur pour x : "))
    if x <= 0:
        print(x ** 2)
    if 0 < x <= 1:
        print(x)
    if 1 < x:
        print(-2 * x + 3)
    

f()