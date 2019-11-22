txt = 'panorama'
set_txt = set(txt)
print(set_txt)

# discard nie wyrzuci błędu jeśli wskażę do usunięcia element nieistniejący w secie.

set_txt.discard('l')
print(set_txt)
# remove wskaże błąd:

set_txt.remove('b')
print(set_txt)