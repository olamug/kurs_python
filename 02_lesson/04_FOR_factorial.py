num = int(input("Podaj jakąś liczbę naturalną nie większą niż 8: "))
pool = list(range(1, num+1))
factorial = 1
print()

if num <= 8:
    print("Kolejne wyniki dla silni cyfry", num)
    for e in pool:
        factorial = factorial * e
        print(factorial)
else:
    print("Błąd! Liczba jest większa od 8.")
