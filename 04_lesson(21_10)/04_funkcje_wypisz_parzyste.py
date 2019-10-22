list = []
counter = int(input("Ile liczb chcesz podać? "))

def is_even():
    for e in range(counter):
        elem = int(input("Podaj swoją liczbę: "))
        if elem % 2 == 0:
            list.append(elem)
        else:
            print("Twoja liczba jest nieparzysta.")
    return list


print(is_even())