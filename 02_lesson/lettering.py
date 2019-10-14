#for step in txt: potem po wcięciu print("-", step)
txt = str(input("podaj słowo: "))
for letter in txt:
    print("-", letter)
names = ["Ada"]
for step in range (3):
    print(step + ":" + names[step])