quote = "Honesty is the first chapter in the book of wisdom."
# Policz wszystkie znaki w napisie
print("Wszystkich znaków w napisie jest", len(quote))
print()
# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])
print()
# Wyświetl tylko pierwszą połowę tekstu
middle = len(quote)//2
print(quote[: middle])
print()
# Wyświetl tylko kropkę
print(quote[-1])
print()
# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[: middle : 3])
print()
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
print()
# Wyświetl cały cytat odwrotnie
print(quote[::-1])
print()
# Zamień wisdom na słowo friendship
print(quote.replace("wisdom", "friendship"))