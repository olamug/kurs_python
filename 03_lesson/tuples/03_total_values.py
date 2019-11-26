users_num = int(input("Podaj swoją liczbę całkowitą w zalresie od 0 do 50, aby sprawdzić czy znajduje się w zbiorze: "))
my_numbers = (2, 14, 44, 5, 2, 11, 7, 13, 22, 31, 50, 39)
print('Moja lista:', my_numbers)

if users_num not in my_numbers:
    print("Twoja liczba nie znajduje się w moim zbiorze.")
else:
    for e in range(len(my_numbers)):
        if my_numbers[e] == users_num:
            print("Twoja liczba znajduje się pod indeksem:", e)

print('********') #trochę prościej
if users_num in my_numbers:
    print("Twoja liczba znajduje się pod indeksem:", my_numbers.index(users_num))
else:
    print("Twoja liczba nie znajduje się w moim zbiorze.")