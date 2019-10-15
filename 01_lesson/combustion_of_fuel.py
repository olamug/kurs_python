distance_km = 120
l_per_100 = 6.4
price = 5.04
total_cost = distance_km * l_per_100 / 100 * 5.04
total_cost = round(total_cost, 2)
print("Całkowity koszt wyprawy wyniesie", total_cost, "zł.")
print()
print("*********WERSJA Z WARTOŚCIAMI UŻYTKOWNIKA*********")
print()
u_distance = int(input("Ile kilometrów ma Twoja trasa? "))
u_l_per_100 = float(input("Spalanie Twojego pojazdu wynosi: "))
u_price = float(input("Cena litra benzyny wynosi: "))
u_fuel_burnt = u_distance * u_l_per_100 / 100
u_total_cost = u_fuel_burnt * u_price
u_total_cost = round(u_total_cost, 2)
print("Całkowity koszt wyprawy wyniesie", u_total_cost, "zł.")