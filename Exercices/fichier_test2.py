import time

a = time.time()

for i in range(1000):
    print(i * 15453 * 151)

b = time.time()

print(b - a)

