import random


def hangman():
    word_list = ['hello', 'world', 'python', 'hackaton']
    random_word = random.choice(word_list)
    letters = list(random_word)
    display = []

    for e in random_word:
        display.append('-')

    print('Guess your word! You\'ve got 11 chances!\n', ' '.join(display))

    counter = 0

    while not display == letters:
        if counter <12:
            users_letter = (input("\nPlease enter your letter:\n").lower())
            for l in range(len(display)):
                if letters[l] == users_letter:
                    display[l] = users_letter
                    print('Got it!', ' '.join(display))
            if users_letter not in letters:
                print('Missed, try again.')
            counter = counter + 1
        else:
            print('You run out of shots. Game over.')
            restart()
    else:
        print('Congratulations! Your word is', ''.join(display))
        restart()


def restart():
    answer = (input('Do you want to play again?\n')).lower()
    if answer == 'yes':
        hangman()
    else:
        print('Goodbye!')


hangman()
