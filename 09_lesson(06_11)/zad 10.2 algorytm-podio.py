# Podaj specyfikacjê zadania, przeanalizuj problem i skonstruuj algorytm w postaci
# program, obliczaj¹cy iloczyn wprowadzanych z klawiatury liczb ca³kowitych, które s¹ ró¿ne od
# zera. Wpisywanie liczb powinno zakoñczyæ siê w momencie, gdy iloczyn przekroczy wartoœæ
# 10 000. Po wykonaniu algorytmu nale¿y wyœwietliæ nastêpuj¹ce informacje:
# a) ile liczb ró¿nych od zera zosta³o wpisanych z klawiatury;
# b) wartoœæ obliczonego iloczynu.

print("Ten program wyœwietli iloczyn podanych liczb ca³kowitych ró¿nych od zera, którego wartoœæ osi¹gnie 10000.")



num_amount = 0
nums_product = 1
while nums_product <= 10000:
    num = int(input("Podaj liczbê do mno¿enia: "))
    nums_product = nums_product * num
    num_amount += 1

print(f"\nIloœæ liczb przemno¿onych: {num_amount}.")
print(f"Wartoœæ iloczynu: {nums_product}.")