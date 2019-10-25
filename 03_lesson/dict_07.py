example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
example_list = tuple(set(example_list))
print(example_list)
print("Najmniejsza liczba w krotce to", min(example_list))
print("Największa liczba w krotce to", max(example_list))