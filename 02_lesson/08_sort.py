num_1 = int(input("Podaj mi pierwszą liczbę: "))
num_2 = int(input("Podaj mi drugą liczbę: "))
num_3 = int(input("Podaj mi trzecią liczbę: "))
print()
if num_1 >= num_2 >= num_3:
    print("Największa liczba to ", num_1,)
    print("Uporządkowane: ", num_1, num_2, num_3)
elif num_1 >= num_2 <= num_3 and num_1 >= num_3:
    print("Największa liczba to ", num_1, )
    print("Uporządkowane: ", num_1, num_3, num_2)
elif num_1 <= num_2 <= num_3:
    print("Największa liczba to ", num_3, )
    print("Uporządkowane: ", num_3, num_2, num_1)
elif num_1 >= num_2 <= num_3 and num_1 <= num_3:
    print("Największa liczba to ", num_3, )
    print("Uporządkowane: ", num_3, num_1, num_2)
elif num_1 <= num_2 >= num_3 and num_3 >= num_1:
    print("Największa liczba to ", num_2, )
    print("Uporządkowane: ", num_2, num_3, num_1)
else:
    print("Największa liczba to ", num_1, )
    print("Uporządkowane: ", num_1, num_2, num_3)