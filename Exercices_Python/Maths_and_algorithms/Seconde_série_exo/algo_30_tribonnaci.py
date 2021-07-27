nums = [0, 1, 1]

def every(k):
    for n in range(1, k):
        nums.append(sum(nums[-n:]))
    return nums


print(every(1))
print(every(2))
print(every(3))
