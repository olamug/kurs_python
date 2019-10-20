sentence = input("Podaj dowolny ciąg znaków. Może zawierać litery każdej wielkości, \ncyfry oraz znaki specjalne. \n")
sen = sentence.replace(" ", '')

counter_l = 0 # dla małych liter
counter_u = 0 # dla wielkich liter
counter_d = 0 # dla cyfr
counter_r = 0 # dla znaków specjalnych
for val in sen:
    if val.isupper():
        counter_u = counter_u + 1
    if val.islower():
        counter_l = counter_l +1
    if val.isdigit():
        counter_d = counter_d +1
    if not val.isalnum():
        counter_r = counter_r + 1

print("W Twoim ciągu znajduje się:")
print(counter_l, "małych liter,")
print(counter_u, "wielkich liter,")
print(counter_d, "cyfr,")
print(counter_r, "znaków specjalnych.")