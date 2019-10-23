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

# druga werjsa porównoywania:
if a > b:
    max_ab = a
else:
    max_ab = b

if max_ab > c:
    max_abc = max_ab
else:
    max_abc = c
return max_abc

x = 3
y = 8
z = 2

result = maximum_of(x, y, z)
print("max of:", x, y, z, "is", result)

# w skróconej wersji porównywanie (operator trójargumentowy)
max_ab = a if a > b else b
max_abc = max_ab if max_ab > c else c

# czwarta metoda cała funkcja
def max_of_2(first, second):
    max_val - first if first > second else second
    return max_val
def maimum_of(a, b, c):
    max_ab = max_of_2(a, b) # jak to usuniemy i walniemy do dołu, to będzie piąta, poniższa metoda
    max_abc = max_of_2(max_ab, c)
    return max_abc

# piąta metoda
def max_of_2(first, second):
    max_val - first if first > second else second
    return max_val
def maimum_of(a, b, c)
    max_abc = max_of_2(max_of_2(a, b), c)
    return max_abc

# a żeby to wszystko skrócić na amen (bo i tak wywolamy później te funkcje)
def max_of_2(first, second):
    max_val - first if first > second else second
def maimum_of(a, b, c)
    max_abc = max_of_2(max_of_2(a, b), c)

#żeby odczytywało wartości od użytkownika:
def read_value():
    return int(input("put intiger value: "))

x = read_value()
y = read_value()
z = read_value()

result = maximum_of(x, y, z)
print("max of:", x, y, z, "is", result)
