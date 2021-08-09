

def inversion(a):
    new = a[-1]
    if len(a) > 1:
        new += inversion(a[0:-1])
    return new

a = "srpssrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnsrpsvnmvsnvnmvsn"
b = inversion(a)
print(b)