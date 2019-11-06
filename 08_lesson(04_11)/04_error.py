import sys


def average(users_list):
    summary = 0
    for e in users_list:
        summary += e
    return summary / len(users_list)


list = input("podaj swoje liczby po przecinku: \n")
list = list.split(',')

print(list)

err_list = []
arr = []
for e in list:
    try:
        arr.append(float(e))
    except (ValueError, TypeError) as exc:
        err_list.append(exc)
        print("Twój błąd to:", exc, sys.exc_info()[0])
        e = 0

# drugi sposób rzutowania na floata: można rzutować bez tworzenia nowej listy
# for index in range(len(list)):
#     list[index] = float(list[index])
# trzeci sposób rzutdowania na floata: enumerate, ale wtedy dziko wyświetli
# for index, elem in enumerate(list):
#     list[index] = float(elem)



# avg = sum(list)/len(list)
# print(avg)

my_average = average(arr)
print('Średnia z podanych wartości to', my_average)
print(err_list)

with open('04_errors_list.txt', 'w', encoding='utf-8') as f:
    f.write('moje błędy\n')
    for r in err_list:
        f.write(str(r)+'\n')
