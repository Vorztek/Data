value = {1 : 1, 2 : 1}

def fibo(n):
    global value
    if not n in value.keys():
        value[n] = fibo(n-1) + fibo(n-2)
    return value[n]

print(fibo(900))