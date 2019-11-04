def is_visa(is_card, number):
    if not is_card: # wcześniej if is_card == False:
        return False
    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_mastercard(is_card, number):
    if not is_card:
        return False
    if is_card and len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(is_card, number):
    if not is_card:
        return False
    if is_card and len(number) == 15:
        if int(number[0:2]) in (34, 37):  # nie trzeba int bo porównujemy 2 stringi, 34 i 37 są w krotce czyli jest to niezmienne co jest w anwiazise
            return True


filename = 'all_cards.txt'
with open(filename, 'r') as f:
    cards = f.readlines()

card_numbers = []
for card_number in cards:
    card_number = card_numbers.append(card_number.strip())

# card_number = (input("Podaj numer karty: "))
can_be_card_number = False

for card_number in card_numbers:
    if len(card_number) < 13 or len(card_number) > 16:
        print("Wrong number")
    else:
        if card_number.isdecimal():
            print("Can be card number")
            can_be_card_number = True
        else:
            print("Not a number")

for card_number in card_numbers:
    if is_visa(can_be_card_number, card_number):
        print("I'm Visa")
        with open('visa.txt', 'a') as v:
            v.write(card_number+'\n')
    elif is_mastercard(can_be_card_number, card_number):
        print("I'm MasterCard")
        with open('mastercard.txt', 'a') as m:
            m.write(card_number+'\n')
    elif is_american_express(can_be_card_number, card_number):
        print("I'm American Express")
        with open('americanexpress.txt', 'a') as a:
            a.write(card_number+'\n')
    else:
        print("Not known card type.")
