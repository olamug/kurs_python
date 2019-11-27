def uppercase_decorator(text):
    def string_capitol():
        return str(text()).upper()
    return string_capitol


@uppercase_decorator
def text_input():
    # string_given = input("Please enter your text.")
    string_given = 'jedzie pociąg jedzie'
    return string_given

# end_result = uppercase_decorator(text_input)
# print(end_result())

print(text_input())