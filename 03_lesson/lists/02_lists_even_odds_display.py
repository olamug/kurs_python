print('This program will display a list of only even odd numbers out of 10 given.')
my_list = []
for e in range(10):
    num = int(input("Pass number: "))
    if num % 2 != 0:
        my_list.append(num)
print("List of provided even odd numbers:", my_list)