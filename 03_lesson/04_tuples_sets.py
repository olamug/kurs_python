list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
counter = 0
for e in list:
    counter = counter + 1
print("Lista składa się z", counter, "elementów.")
size_short = counter / 3
short_1 = []
while len(short_1) < size_short:
    for e in list:
        short_1 = short_1.append(e)
        print(short_1)