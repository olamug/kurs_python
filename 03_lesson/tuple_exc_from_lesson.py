# Policz elementy na liœcie, dopóki element nie bêdzie krotk¹.
my_tuple = ('a', 4.3, 77, 3j+4)
tmp_list = list(my_tuple)
tmp_list.remove(77)
print(tmp_list)
my_tuple = tuple(tmp_list)
print()
print("#####################################")
print()
numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
    if isinstance(n, tuple):
        break
    counter = counter + 1
print(counter)
