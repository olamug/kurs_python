my_tuple = ('Christmas', 44, 'Python', 502, 44, 44, 'Pink Panther', "Python", '963')
print("Moja krotka:", my_tuple)
print("***")
answers = []
for e in my_tuple:
    count_element = my_tuple.count(e)
    if count_element > 1:
        answers.append(f'Element \'{e}\' pojawił się na liście {count_element} razy.')

a = [print(i) for i in set(answers)]
print("*******************************************")
# drugi sposób z collections
from collections import Counter

my_tuple = ('Christmas', 44, 'Python', 502, 44, 44, 'Pink Panther', "Python", '963')
print('Moja krotka:', my_tuple)
counter = dict(Counter(my_tuple))
print('Licznik elementów:',counter)

for k, v in counter.items():
    if v > 1:
        print(f'Element \'{k}\' pojawił się na liście {v} razy.')