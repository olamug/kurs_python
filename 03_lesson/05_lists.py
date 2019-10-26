# zadanie 5
people = [
    # ['imię', 'nazwisko', 'zawód'],
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]
# print(people)
# # for element in list(list3x5):
# #     print(people[element][0], people[element][1], people[element][2])
# for row in people:
#     print(row[0], row[1], row[2])
# print()
# print("--------------------------------------------------")
# print()
# #jeszcze inna metoda
print("liczba ludzi: ", len(people))
for row in range(len(people)):
    # print(row)
    for col in people[row]:
        print(col, end=' ')
    print()
print()
print("--------------------------------------------------")
print()
# #inaczej wersja hard
# for row in range(len(people)):
#     for col in range(len(people[row])):
#         if col == 1:
#             print(people[row][col], end = ' - ')
#         else:
#             print(people[row][col], end = ' - ')
#     print()
# print()
# print("--------------------------------------------------")
# print()
# #jeszcze gorzej
# for row in range(len(people)):
#     # print()
#     for col in range(len(people[row])):
#         if col == 1:
#             print(people[row][col], end = ' - ')
#         elif col == 2:
#             print(people[row][col], end = ' * ')
#         else:
#             print(people[row][col], end = ' - ')
#     print() #można dodać go po pierwszym for (przed drugim)