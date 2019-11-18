names = input("Podaj imiona osób, które chcesz powitać oddzielone spacją!")
names = names.split()
for e in names:
    e = e.capitalize()
    print("Hello", e+'!')
