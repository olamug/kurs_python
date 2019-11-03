def num_in_range():
    users_range = range(x, y+1)
    if num in users_range:
        print(f'Tak, {num} znajduje się w zadanym zakresie.')
    else:
        print(f'Nie, {num} jest spoza zakresu.')


num = 5
x = int(input('Podaj zakres od: '))
y = int(input('Podaj zakres do: '))
num_in_range()


# druga niepotrzebnie skomplikowana wersja ale z dwoma funkcjami (przekazanie zmiennej)
# def num_in_range(rang):
#     if num in rang:
#         print(f'Tak, {num} znajduje się w zadanym zakresie.')
#     else:
#         print(f'Nie, {num} jest spoza zakresu.')
#
#
# def range_maker(x, y):
#     return range(x,y+1)
#
#
# x = int(input('Podaj zakres od: '))
# y = int(input('Podaj zakres do: '))
# num = 5
# users_range = range_maker(x, y)
# num_in_range(users_range)
