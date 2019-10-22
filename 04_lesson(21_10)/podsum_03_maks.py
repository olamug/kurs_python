print("Ten *program* podaje największą spośród trzech liczb.")
def maximum_of(a, b, c):
    if a > b > c or a > c > b:
        print(a)
    elif b > a > c or b > c > a:
        print(b)
    else:
        print(c)

num_1 = int(input("Podaj pierwszą liczbę: "))
num_2 = int(input("Podaj drugą liczbę: "))
num_3 = int(input("Podaj trzecią liczbę: "))
print("Największą liczbą jest: ",)
maximum_of(num_1, num_2, num_3)
