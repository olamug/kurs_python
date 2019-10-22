def circle_field(radius):
    pi = 3.14
    return pi * radius ** 2

r = float(input("podaj promień koła: "))
print("Pole powierzchni wynosi: ", circle_field(r))