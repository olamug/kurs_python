my_tuple_1 = (1, 'ladino music', 7, 6, 'elephant', 'tattoo', 879)
my_tuple_2 = ('Christmas', 'Python', 502, ('Adam', 'Eve'), 44, 'Pink Panther', '963')

final_arr = []

for e in range(len(my_tuple_1)):
    if e % 2 == 0:
        final_arr.append(my_tuple_1[e])

for i in range(len(my_tuple_2)):
    if i % 2 != 0:
        final_arr.append(my_tuple_2[i])

print(final_arr)

