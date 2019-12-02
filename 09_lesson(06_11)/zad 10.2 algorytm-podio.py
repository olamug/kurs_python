# Podaj specyfikacj� zadania, przeanalizuj problem i skonstruuj algorytm w postaci
# program, obliczaj�cy iloczyn wprowadzanych z klawiatury liczb ca�kowitych, kt�re s� r�ne od
# zera. Wpisywanie liczb powinno zako�czy� si� w momencie, gdy iloczyn przekroczy warto��
# 10 000. Po wykonaniu algorytmu nale�y wy�wietli� nast�puj�ce informacje:
# a) ile liczb r�nych od zera zosta�o wpisanych z klawiatury;
# b) warto�� obliczonego iloczynu.

print("Ten program wy�wietli iloczyn podanych liczb ca�kowitych r�nych od zera, kt�rego warto�� osi�gnie 10000.")



num_amount = 0
nums_product = 1
while nums_product <= 10000:
    num = int(input("Podaj liczb� do mno�enia: "))
    nums_product = nums_product * num
    num_amount += 1

print(f"\nIlo�� liczb przemno�onych: {num_amount}.")
print(f"Warto�� iloczynu: {nums_product}.")