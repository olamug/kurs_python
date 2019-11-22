my_tuple = ('Christmas', 44, 'Python', 502, 44, 44, 'Pink Panther', "Python", '963')


answers = []
for e in my_tuple:
    count_element = my_tuple.count(e)
    if count_element > 1:
        answers.append(f'Element \'{e}\' pojawił się na liście {count_element} razy.')

[print(i) for i in set(answers)]
print("**********")
