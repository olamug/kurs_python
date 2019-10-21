print("Sprawdź czy dwa środkowe elementy wyrażenia są takie same!")
elements = int(input("Ile chcesz podać wyrazów/elementów? "))
while elements % 2 == 1:
    elements = int(input("Musi to być parzysta liczba. Podaj jeszcze raz: "))

list = []
for e in range(elements):
    elem = input("Podaj wyraz/element: ")
    list.append(elem)

middle = int(len(list)/2)
mid1 = list[middle]
mid2 = list[middle-1]

if mid1 == mid2:
    print("Dwa środkowe wyrazy/elementy, które podałeś są takie same.")
else:
    print("Dwa środkowe wyrazy/elementy, które podałeś nie są takie same.")