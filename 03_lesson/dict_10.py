print("Gdy podasz wybraną liczbę, wyświetlę kwadraty każdej poprzedniej i wybranej.")
n = int(input("Jaką liczbę chcesz podać? "))
dict = {}
for e in range(1, n+1):
    dict[e] = e**2
print(dict)
