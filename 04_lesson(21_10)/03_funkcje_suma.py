def adding_num():
    counter = int(input("Ile chcesz dodać liczb? "))
    summ = 0
    for e in range(counter):
        elem = int(input("Dodaj kolejną liczbę: "))
        summ = summ + elem
    return summ


print("Suma podanych liczb wynosi", adding_num())
