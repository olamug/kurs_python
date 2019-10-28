import random

filename1 = '20_quotes_text.txt'
filename = input("Please insert name of file with its extension containing your quotes: \n")
print("Quote of the day is:\n")

with open(filename, 'r', encoding='utf-8') as fopen:
    lines_list = fopen.readlines()

quote = random.choice(lines_list).strip()
quote1 = quote.split(' - ')
stars = '*' * len(quote)
print(stars)
print(quote1[0]) # jakby ustawić na sztywno ilość większą gwiazdek to quote.center(ilość gwiazdek)
print(('~ ' + quote1[1]).center(len(quote))) # + bo inaczej potraktuje to jako tuple (~, autor) jakby był przecinek i wyskoczy błąd dla center
print(stars)