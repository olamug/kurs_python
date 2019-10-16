# Zdanie "Kobyła ma mały bok"
print("Czy zdanie 'Kobyła ma mały bok' jest palindromem?")
sen1 = "Kobyła ma mały bok"
sen1 = sen1.lower()
sen1 = sen1.replace(" ", "")
sen1_back = (sen1[::-1])
print("Odpowiedź: ", sen1 == sen1_back)
print()
# WERSJA DLA UŻYTKOWNIKA
print("SPRAWDŹ, CZY TWOJE ZDANIE JEST PALINDROMEM")
sen = input("Podaj swoje zdanie: ")
sen = sen.lower()
sen = sen.replace(" ", "")
sen_back = (sen[::-1])
print("Czy Twoje zdanie jest palindromem? ", sen == sen_back)