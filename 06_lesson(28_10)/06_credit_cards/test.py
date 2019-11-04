
filename = 'all_cards.txt'
with open(filename, 'r+') as f:
    card_number = f.readlines()

print(card_number)