import random

print("Gra ciep³o-zimno! Zgadnij ukryt¹ liczbê! Masz 6 szans. Powodzenia!")

number = random.randint(0, 100)
guesses = 0
if guesses < 7:
    guess = int(input('Podaj liczbe w zakresie od 0 do 100: '))
    if number - 10 < guess < number + 10 and number != guess:
        print('Ciep³o...')
    elif guess == number:
        print('Wygra³eœ!')
    else:
        print('Zimno')
    guesses = guesses + 1
else:
    print('Wykorzysta³eœ wszystkie szanse. Komputer wygra³!')
