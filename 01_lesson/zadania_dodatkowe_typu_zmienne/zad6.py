# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("Sprawdź czy Twoja lodówka zmieści się do windy by ją bezpiecznie zwieźć.")
print()
fridge_h = int(input("Podaj wysokość lodówki w centymetrach: "))
fridge_w = int(input("Podaj szerokość lodówki w centymetrach: "))
fridge_d = int(input("Podaj długość lodówki w centymetrach: "))
print()
elev_h = int(input("Podaj wysokość windy w centymetrach: "))
elev_w = int(input("Podaj szerokość windy w centymetrach: "))
elev_d = int(input("Podaj długość windy w centymetrach: "))
print ()
fridge_vol = fridge_d * fridge_h * fridge_w
elev_vol = elev_d * elev_h * elev_w
print("Czy Twoja lodówka zmieści się w windzie? Odpowiedź:", fridge_vol < elev_vol)
