names = input("Podaj imiona osób, które chcesz powitać oddzielone spacją!")
names = names.split()
for name in names:
    print("Hello ", name, "!")
