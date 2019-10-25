poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.replace(',', '').lower()

poem = poem.split()

dict = {}
counter = 0
for w in poem:
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1

for k, v in dict.items():
    if k == "szybko":
        print(k, ':', v)
    elif k == "zbudź":
        print(k, ':', v)