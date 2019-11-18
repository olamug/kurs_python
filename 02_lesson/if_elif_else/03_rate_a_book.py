print("Jaką ocenę ma książka w skali 1-10?")
rate_1 = int(input("Podaj ocenę okładki: "))
rate_2 = int(input("Podaj ocenę stylu pisania: "))
rate_3 = int(input("Podaj ocenę fabuły: "))
avg = round(((rate_1 + rate_2 + rate_3)/3), 1)
print()
if avg >= 7:
    print("Twoja ocena to", avg, "Bardzo dobry")
elif avg >= 5:
    print("Twoja ocena to", avg, "Przeciętna")
else:
    print("Twoja ocena to", avg, "Nie warta uwagi")