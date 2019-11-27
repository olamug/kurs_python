def example_function():
    a = 7
    def nested_function(age):
        print('Jestem w środku zagnieżdżenia')
        return a*age
    return nested_function


new_function = example_function()  # to jest tak jakby nested function, wywołanie new_function z (), # dodaje () do nested_function

new_function()