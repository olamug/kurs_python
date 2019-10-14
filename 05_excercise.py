print("Ustaw hasło składające się z cyfr i liter, o długości co najmniej 8 znaków i zawiera co najmniej 1 dużą literę.")
password = input("Wprowadź swoje hasło: ")
alphanum = password.isalnum()
condition_1_upper = alphanum and password.islower()

if len(password) < 8:
    print("Złe hasło. Hasło powinno zawierać co najmniej 8 znaków.")
if not alphanum:
    print("Złe hasło. Powinno zawierać cyfry i litery.")
if password.isalpha():
    print("Złe hasło. Powinno zawierać co najmniej jedną cyfrę.")
if password.isdigit():
    print("Hasło musi zawierać przynajmniej jedną literę.")
if condition_1_upper:
    print("Hasło musi zawierać co najmniej jedną wielką literę.")

print("End")