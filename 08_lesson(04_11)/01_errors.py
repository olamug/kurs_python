import sys

list = [13, 'string', 2+3j, 0, 2.45, True, ('one', 'two'), {1, 2, 3}, {'apple':1, "cucumber":2}]

for elem in list:
    try:
        result = 10 / elem
    except ZeroDivisionError as e:
        result = "wyjątek 1:", e
    except TypeError as e:
        result = "Wyjątek 2:", e
    print(result)

# ŹŹŹŹLLLLLLLLEEEEEEEEEEEEEEEEEEE!!!!!!!!!!
# def list_division():
#     for i in list:
#         if not type(i) == 'int':
#             raise ValueError("To nie jest wartość liczbowa!")
#         else:
#             result = i / 10
#         print(result)
#
#
# try:
#     list_division()
# except ValueError as ex:
#     print(ex)
# except Exception:
#     print("Jakiś inny błąd: ", sys.exc_info([0]))
