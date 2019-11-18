#for step in txt: potem po wcięciu print("-", step)
txt = str(input("podaj słowo: "))
for letter in txt:
    print("-", letter)
names = ["Ada", "Julia", "Ruby"]
for e in range(len(names)):
    print("id:", e, "name:", names[e])