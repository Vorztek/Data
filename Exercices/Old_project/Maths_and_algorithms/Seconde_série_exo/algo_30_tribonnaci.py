nums = [0, 1, 1]

def every(k):
    for n in range(1, k):
        nums.append(sum(nums[-n:]))
    return nums


""" print(every(1))
print(every(2))
print(every(3)) """

def compte(n):
    for i in range(n):
        a = every(i)

    return a


print(compte(1000))