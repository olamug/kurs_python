def triangle_field(base, height):
    print('Pole trójkąta')
    field = 0.5 * base * height
    return field


def square_field(height):
    print('Pole kwadratu')
    field = height**2
    return field


def trapeze_field(base1, base2, height):
    print('Pole trapezu')
    field = (base1 + base2) * height / 2
    return field


def circle_field(radius):
    print('Pole koła')
    field = 3.14159265 * (radius ** 2)
    return field
print("Pola figur")
print("dodatkowy jakiś napis poza funkcjami")



# print(triangle_field(a, h))
