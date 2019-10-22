def is_even(num):
    if num % 2 == 0:
        print("Twoja liczba jest parzysta.")
    else:
        print("Twoja liczba jest nieparzysta.")


my_num = int(input("Podaj liczbę, by sprawdzić czy jest parzysta: "))
print(is_even(my_num))
