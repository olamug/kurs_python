# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

print("Witamy w kantorze \"Python\". Przelicz złotówki na euro i dolary.")
print()
euro_course = 4.27972524
dollar_course = 3.83316531
money = int(input("Podaj ile pieniędzy (złotych) planujesz zabrać na wakacje? "))
euros = round(money/euro_course)
dollars = round(money/dollar_course)
print()
print("Twoje pieniądze w przeliczeniu to", euros, "euro, lub", dollars, "dolarów (bez eurocentów i centów, \nktóre mogą się różnić w zależności od wybranego kantoru.")
bill_50 = euros // 50
bill_20 = (euros % 50) // 20
rest_20 = (euros % 50) % 20
bill_10 = rest_20 // 10
rest_10 = rest_20 % 10
coin_5 = rest_10 // 5

print("Możemy tę sumę przekaząc w następującej formie gotówki:")
print(bill_50, "banknotów po 50 euro \n", bill_20, "banknotów po 20 euro \n", bill_10, "banknotów po 10 euro \n", coin_5, "monet po 5 euro \n")
print("U nas przelicznik jest najkorzystniejszy i można negocjować większe sumy! \nMy węża w kieszeni nie nosimy! \nZapraszamy! Kantor Python")