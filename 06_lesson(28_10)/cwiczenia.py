filename = 'tekst.txt'

# with open(filename, 'r') as fopen:
#     content = fopen.read()
#     print(content)
#
# print("Koniec")

# czytanie po jednej linii - nie za dobra metoda:
#
# with open('tekst.txt', 'r') as fopen:
#     while True:
#         current_line = fopen.readline()
#
#     # aktualna linia jest pusta
#         if current_line == '':
#       # dotarlismy do konca
#             break
#         print(current_line)

# czytanie linijka po linijce - dobra opcja, tj. zapisanie linijek do
# zmiennej lines - tablicy, którą można przywoływać jak zwykłą listę.
with open(filename, 'r', encoding='utf-8') as fopen:
    content = fopen.read()
print(content)
    # lines = fopen.readlines() # to po odczytaniu czyli open with as fopen robi listę lines
# print(lines) # <--- zwykłe wyprintowanie listy
# for l in lines:
#     print("Line", l)

# for l in range(len(lines)): # można dać in range(4), ale poniżej ma być właśnie indeks, czyli lines [l]
#     print("Line " + str(l), lines[l].strip('\n'))
# #   print("Line " + str(l), lines[l].strip('\n'), end = '*')

# with open('save.txt', 'w') as f:
#     f.write('Line 1\n')
#     f.write('Line 2\n')
#     f.write('Line 3\n')
#     f.write('Line 4\n')
