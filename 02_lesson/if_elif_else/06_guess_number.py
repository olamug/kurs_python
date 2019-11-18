# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą
# przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl
# “pudło!”.
print("Zgadniesz jaką liczbę ukryłam?")
print()
my_num = 14
num = int(input("Podaj swoją liczbę od 0 do 100: "))
if num == my_num:
    print("gratulacje")
else:
    print("pudło!")