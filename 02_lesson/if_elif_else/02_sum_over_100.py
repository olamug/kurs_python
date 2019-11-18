print = ("Sprawdź, czy suma Twoich liczb jest większa niż 100?")
num_1 = int(input("Podaj pierwszą liczbę: "))
num_2 = int(input("Podaj drugą liczbę: "))
sum = num_1 + num_2
if sum < 100:
    print(sum)
else:
    print("Koniec")