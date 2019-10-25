list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
counter = 0
for a in list:
    counter = counter + 1
print("Lista składa się z", counter, "elementów.")

size_short = counter / 3

short_1 = []
short_2 = []
short_3 = []

for e in list:
    if list.index(e) < size_short:
        short_1.append(e)
    elif list.index(e) >= size_short and list.index(e) <size_short*2:
        short_2.append(e)
    else:
        short_3.append(e)

short_1.reverse()
short_2.reverse()
short_3.reverse()

print(short_1)
print(short_2)
print(short_3)