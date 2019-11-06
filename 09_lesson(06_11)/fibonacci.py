def suma_for(n):
    num = 0
    for i in range(1, n+1):
        num = num + i
    return num


n = 10
print(suma_for(n))


def suma_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s

print(suma_while(10))

def suma_recursion(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursion(n-1)


print(suma_recursion(10))