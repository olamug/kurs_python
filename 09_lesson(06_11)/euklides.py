def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


def nww(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a


a = 60
b = 48

print(nwd(a, b))
print("**********")
print(nww(a, b))