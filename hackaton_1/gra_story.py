# ### Historyjka a'la RPG:
# - Konieczność użycia modułu `random`.
# - Program wypisuje kolejne "przygody" bohatera.
# - Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami, np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
# - Historyjka ma mieć zadaną długość i ma być możliwie losowa.
import random
names = ['Nubill', 'Alojra', 'Korgun', 'Polien', 'Karmeron', 'Korn']
chosen_name = random.choice(names)
print(chosen_name)

place = input("Do you want to go to the forest? insert F or to the town - insert T? \n")

market_products = ['potatoes', 'tomatoes', 'strawberries', 'onion', 'raw fish']
product = random.choice(market_products)
quantity_food = random.randrange(1, 15)
quantity_days = random.randrange(1, 15)
forrest_food = {'b' : 'blueberries 🍒', 'mm' : 'blackberries 🍇', 'm' : 'mushrooms 🍄'}
def death():
    print("you've just died. end of game")

def forest_place():
    answear = input(f'{chosen_name}, are you hungry? - asked unknown voice.Y/N')
    if answear == 'y':
        forrest_choice = input('What would you like to eat my friend? B - blackberries, BB - blueberries, M - mushrooms')
        print(f"Here you are some {forrest_food[forrest_choice]}, eat it sweetheart, they're delicious")
        if forrest_choice.lower() == 'm':
            death()
    else:
        print("Maybe next time, you know where to find me.")


def town_place():
    print(f'{chosen_name}, went to the market place and got {quantity_food} of {product}.')
    print(f"This will be his food for the next {quantity_days} days.")
    if quantity_days >= 4:
        print(f'{chosen_name} walks for 2 days to the forest and search for something to eat, because this isn\'t enough food for him to survive')
        forest_place()
        print()
    else:
        print("You have to steal something.")


if place.lower() == "f":
    forest_place()
elif place.lower() == "t":
    town_place()


def try_again():
    again = input('Chcesz zagrać jeszcze raz? ')
    if again.lower() == 'tak':
        guess_game()
    else:
        print(f"You did well {chosen_name}! May we meet again")
        exit()
