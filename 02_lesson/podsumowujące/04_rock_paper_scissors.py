import random

rounds_select = int(input("How many rounds would you like to play with CPU:\n"))
choices = ['rock', 'paper', 'scissors']

users_scores = 0
comp_scores = 0
round_counter = 0

while round_counter < rounds_select:
    comp_choice = random.choice(choices)
    users_choice = input("Choose your pick: rock, paper, scissors or type 'exit' to quit the game.\n")

    if users_choice == comp_choice:
        print(f'Computer also picked {comp_choice}, it\'s a draw!')
    elif users_choice == 'rock' and comp_choice == 'scissors':
        print(f'Computer picked {comp_choice}. You win!')
        users_scores += 1
    elif users_choice == 'paper' and comp_choice == 'rock':
        print(f'Computer picked {comp_choice}. You win!')
        users_scores += 1
    elif users_choice == 'scissors' and comp_choice == 'paper':
        print(f'Computer picked {comp_choice}. You win!')
        users_scores += 1
    elif users_choice == 'exit':
        print('See you next time!')
        exit()
    else:
        print(f'Computer picked {comp_choice}. Computer wins!')
        comp_scores += 1
    round_counter += 1
print()
print("***TOTAL SCORE***")
print("Users score:", users_scores)
print("CPU's score:", comp_scores)

if users_scores > comp_scores:
    print("***Congratulations, you won the game!***")
elif comp_scores > users_scores:
    print("***Sorry, but this time CPU won the game!***")
else:
    print("***It's a draw. Maybe next time you'll win the game!***")