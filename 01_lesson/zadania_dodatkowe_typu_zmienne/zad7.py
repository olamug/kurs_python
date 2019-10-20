# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("Witamy w kantorze \"Python\". Przelicz złotówki na euro i dolary.")
print()
euro_course = 4.27972524
dollar_course = 3.83316531
money = int(input("Podaj ile pieniędzy (złotych) planujesz zabrać na wakacje? "))
euros = round(money/euro_course)
dollars = round(money/dollar_course)
print()
print("Twoje pieniądze w przeliczeniu to", euros, "euro, lub", dollars, "dolarów (bez eurocentów i centów, \nktóre mogą się różnić w zależności od wybranego kantoru. \nU nas przelicznik jest najkorzystniejszy i można negocjować większe sumy! \nMy węża w kieszeni nie nosimy! \nZapraszamy! Kantor Python")