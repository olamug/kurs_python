import random


def random_3_quotes():
    quote = random.choice(lines_list).strip()
    quote1 = quote.split(' - ')
    return quote1


def show(quote1):
    stars = '*' * len(quote1[0])
    print(stars)
    print(quote1[0])  # jakby ustawić na sztywno ilość większą gwiazdek to quote.center(ilość gwiazdek)
    print(('~ ' + quote1[1]).center(len(quote1[0])))  # + bo inaczej potraktuje to jako tuple (~, autor) jakby był przecinek i wyskoczy błąd dla center
    print(stars)


filename1 = '20_quotes_text.txt'
# filename = input("Please insert name of file with its extension containing your quotes: \n")
print("Quote of the day is:\n")

with open(filename1, 'r', encoding='utf-8') as fopen:
    lines_list = fopen.readlines()

for i in range(3):
    sentence = random_3_quotes()
    print('--------')
    show(sentence)
