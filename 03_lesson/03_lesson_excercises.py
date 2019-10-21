
# zadanie 3
list_num = input("Podaj listę liczb całkowitych: ")
print("Sprawdzam, czy ostatni i pierwszy element jest taki sam: ")
print(list_num[0] == list_num[-1])
print()
#inna - lepsza wersja zadania 3
counter = int(input("Ile lizb chcesz dodać?: "))
elements = []
for i in range(counter):
    e = input("poodaj dowolny ciąg znaków: ")
    elements.append(e)

print(elements)
print("czy pierwszy i osattni są takie sam:", elements[0] == elements[-1])
if elements[0] == elements[-1]:
    print("pierwszy i osattni są takie smae")
else:
    print("elementy nie są takie same")

#jeszcze inny sposó
elements2 = []
counter2 = 5
while counter2 > 0:
    e =input()
    elements2.append(e)
    counter2 -= 1

print(elements2)

# JESZCZE INACZEJ DOPÓKI KTOS NIE WCIŚNIE JAKIEGOŚ PRZYCISKU NIECHCIANEGO
num_arr = []
while True:
    e = input("Podaj nowy element. naciśniij q aby zakończyć")
    if e == "q":
        break
    num_arr.append(e)
print(num_arr)