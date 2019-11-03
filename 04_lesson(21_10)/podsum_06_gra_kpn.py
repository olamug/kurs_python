import random


def main_game(users_choice, comp_choice):
    if users_choice == comp_choice:
        print(f'Computer also picked {comp_choice}, it\'s a draw!')
        return 'draw'
    elif winning_options[users_choice] == comp_choice:
        print(f'Computer picked {comp_choice}. You win!')
        return 'win'
    else:
        print(f'Computer picked {comp_choice}. Computer wins!')
        return 'lost'


def game_scores():
    users_scores = 0
    comp_scores = 0
    shots_counter = 5
    for e in range(shots_counter):
        users_choice = input("Choose your pick: rock, paper or scissors:\n")
        comp_choice = random.choice(choices)
        if main_game(users_choice, comp_choice) == 'win':
            users_scores += 1
        elif main_game(users_choice, comp_choice) == 'lost':
            comp_scores += 1
        shots_counter -= 1
        print(f'You have {shots_counter} chances left')
    return users_scores, comp_scores


def total_scores(user, comp):
    if user > comp:
        print(f'Total score is {user} for you and {comp} for computer. \n You won!')
    elif user < comp:
        print(f'Total score is {comp} for computer and {user} for you. Computer won.')
    else:
        print(f'Total score is {user} to {comp}. It\'s a draw!')


choices = ['rock', 'paper', 'scissors']
winning_options = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

(user, comp) = game_scores()

total_scores(user, comp)
