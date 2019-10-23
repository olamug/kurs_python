# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję
# obliczającą bmi na podstawie danych użytkownika oraz zwracającą
# odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru

def calc_bmi(weight, height):
    return weight / height ** 2

def bmi_status(bmi):
    if bmi < 18.49:
        print('Your BMI is:', bmi, "- underweight.")
    elif bmi < 24.99:
        print('Your BMI is:', bmi, "- normal (healthy) weight.")
    elif bmi < 29.99:
        print('Your BMI is:', bmi, "- overweight.")
    else:
        print('Your BMI is:', bmi, "- obesity.")

weight = float(input("How much do you weight? "))
height = float(input("How tall are you? (Height in meters) "))

bmi = round(calc_bmi(weight, height), 1)
print(bmi)
bmi_status(bmi)

# W DOMU ROBIONE
def convert(miles):
    return 1.609 * miles
distance = int(input("podaj liczbę mil: "))
miles = convert(distance)
print(miles)

# silnia

def obliczsilnie(a):
    i = 1
    pytanie = input("napisz kot: ")
    silnia = 1
    while i < a:
        i += 1
        silnia = silnia * i
    return(silnia, pytanie)

wynik = obliczsilnie(4)
print(wynik)

#też działająca druga wersja obliczania pola powierzchni koła
def circle_field():
    pi = 3.14
    r = int(input("Podaj promień: "))
    return pi*r**2

print(circle_field())