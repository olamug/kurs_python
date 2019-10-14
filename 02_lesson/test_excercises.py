names = input("Podaj imiona osób, które chcesz powitać oddzielone spacją! ")
names = names.split()
id = 0
while id < len(names):
    print("Hi", names[id])
    id = id +1