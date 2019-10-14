print("Jaką ocenę ma książka?")
rate_1 = int(input("Podaj ocenę: "))
rate_2 = int(input("Podaj ocenę: "))
rate_3 = int(input("Podaj ocenę: "))
avg = (rate_1 + rate_2 + rate_3)/3
print()
if avg >= 7:
    print("Bardzo dobry")
elif avg >= 5:
    print("Przeciętna")
else:
    print("Nie warta uwagi")