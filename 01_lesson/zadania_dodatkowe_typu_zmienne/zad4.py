# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("Podaj 3 dowolne liczby całkowite; dwie pierwsze pomnożę a potem je podzielę przez trzecią.")
num_1 = int(input("Podaj pierwszą z trzech lizczb całkowitych: "))
num_2 = int(input("Podaj drugą z trzech lizczb całkowitych: "))
num_3 = int(input("Podaj trzecią z trzech lizczb całkowitych: "))
print()
multiplying = num_1 * num_2
ratio = multiplying / num_3
print("Iloczyn dwóch pierwszych liczb wynosi", multiplying, "\nUzyskany wynik teraz podzielę przez trzecią liczbę.")
print()
print("Iloraz poprzedniego iloczynu i trzeciej podanej liczby wynosi w zaokrągleniu", round(ratio, 2))