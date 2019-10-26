import random
names = ['Nubill', 'Alojra', 'Korgun', 'Polien', 'Karmeron', 'Korn']
chosen_name = random.choice(names)
print(f"The stars chosen to send {chosen_name} to the unknown lands and see if he can face it's dangers! "
      f"\nLet the game begin!")
print()

market_products = ['potatoes', 'tomatoes', 'strawberries', 'onion', 'raw fish']
product = random.choice(market_products)
quantity_food = random.randrange(1, 15)
quantity_days = random.randrange(1, 15)
forest_food = {'B': 'blueberries 🍒', 'BB': 'blackberries 🍇', 'M': 'mushrooms 🍄'}
stolen_items = ['cat', 'dog', 'gold earings', 'necklace', 'old shirt', 'brush', 'king\'s lost crown', 'empty casket']
stolen_dict = {}
stolen_list = []


def init_game():
    place = input("Do you want to go to the forest? insert F for forest or T for town? \n")
    if place.lower() == "f":
        forest_place()
    elif place.lower() == "t":
        town_place()


def try_again():
    again = input('Do you want to play again? Y/N')
    if again.lower() == 'Y':
        init_game()
    else:
        print("May we meet again.")
        exit()


def forest_place():
    answear = input(f'{chosen_name}, are you hungry? - asked unknown voice.Y/N \n')
    if answear == 'y':
        forest_choice = input('What would you like to eat my friend? B - blackberries, BB - blueberries, M - mushrooms\n')
        print(f"Here you are some {forest_food[forest_choice.upper()]}, eat it sweetheart, they're delicious")
        if forest_choice.lower() == 'm':
            print(f'Unfortunately, the {forest_food[forest_choice.upper()]} was poisonous.')
            death()
        else:
            wizzard(forest_food[forest_choice.upper()], wizzard_name = "Alindur", location="wilderness")
    else:
        print("Maybe next time, you know where to find me.")
        print(f"{chosen_name} had to steal some food so eventually went to the town.")
        town_place()


def wizzard(food, wizzard_name, location):
    sentence = f"{chosen_name} met {wizzard_name.capitalize()}, the great wizzard who showed on his path in {location}."
    print(sentence)
    print("The wizzard told a story about very greevy dragon, who has been stealing treasures from people for years. "
          "Whoever gets to kill the beast, will become the richest man on lands.")
    kill_dragon = input(f"Does {chosen_name} want to kill the dragon? Y/N\n")
    if kill_dragon.lower() == 'y':
        print(f"Nobody has beaten the dragon yet. Neither did {chosen_name}")
        death()
    else:
        print(f"{chosen_name} lived long and happily yet lonely eating {food} for the rest of his life.")
        try_again()


def town_place():
    print(f'{chosen_name} went to the market place and got {quantity_food} of {product}.')
    print(f"This will be his food for the next {quantity_days} days.")
    if quantity_days >= 13:
        print(f'{chosen_name} walks for 2 days to the forest and search for something to eat, because this '
              f'isn\'t enough food for him to survive')
        forest_place()
        print()
    else:
        print(f"{chosen_name} has to steal something to survive in the town.")
        quantity_of_houses = int(input('He needs to decide how many houses he is going to rob.'))
        for i in range(quantity_of_houses):
            stolen_things = random.choice(stolen_items)
            stolen_list.append(stolen_things)
            if stolen_things in stolen_dict:
                stolen_dict[stolen_things] += 1
            else:
                stolen_dict[stolen_things] = 1
        print(f'{chosen_name} has stolen:')
        for key, values in stolen_dict.items():
            print(values, key, end=', ')
            print()
        # if 'gold earings' or 'necklace' or 'king\'s lost crown' in stolen_dict.keys():
        print(f'{chosen_name} got really lucky and lived long in wealth from now on. '
              f'His mission is complete! End of game.')
        try_again()

        # else:
        #     print(f'{chosen_name} wasn\'t a very good thief, but eventually he could buy something to eat.')


def death():
    print(f"Unfortunately {chosen_name} has just died. \nGame over.")
    try_again()


def try_again():
    again = input('Do you want to play again? ')
    if again.lower() == 'tak':
        init_game()
    else:
        print(f"May we meet again!")
        exit()


init_game()
