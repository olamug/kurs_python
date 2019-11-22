my_list = [['#'] * 3] * 4
print(my_list)

print()

for row in range(4):
    for col in range(3):
            print(my_list[row][col], end = ' ')
    print()
