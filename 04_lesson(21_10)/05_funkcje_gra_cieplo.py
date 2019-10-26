import random

print("Zgadnij ukrytą liczbę! Masz 10 szans. Powodzenia!")

def main():
    guess_game()
    try_again()


def guess_game():
    number = random.randint(0, 100)
    guesses = 0
    while guesses < 10:
        guess = int(input('Podaj liczbe w zakresie od 0 do 100: '))
        if number - 10 < guess < number + 10 and number != guess:
            print('Ciepło...')
        elif guess == number:
            print('Wygrana!')
            break
        else:
            print('Zimno')
        guesses = guesses + 1
    try_again()


def try_again():
    again = input('Chcesz zagrać jeszcze raz? ')
    if again.lower() == 'tak':
        guess_game()
    else:
        print("Do zobaczenia!")
        exit()


guess_game()