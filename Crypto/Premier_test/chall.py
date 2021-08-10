def encryption(f):
    ct = []
    for char in f:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)



f = open('msg.enc','w')
ct = encryption(f)
print(ct)
""" f.write(ct.hex())
f.close()
 """
