# TYPE ERROR
# x = 'ala' + 3
# print(x)
# input("lslslsl", 3, 4)
# ZERO DIVISION ERROR
# res = 4/0
# NAME ERROR
# name = Rita
# SYNTAX - NIE DO KOŃCA WYJĄTEK
# FileNotFoundError
# f = open("lalala.txt")
# content = f.read()
# lista = [2, 'apple']
# object = lista[0].strip()
# print(object)
# my_tuple = ('flower', 'tree')
# my_tuple[1] = 'cat'
# dict = {'phone':'samsung', 'speakers':'denon'}
# print = dict[1]
#
#
# try:
#     x = float(input("podaj liczbę: "))
#     result = 4 / x
# except ValueError as e:
#     print(e)
#
# except (TypeError, ZeroDivisionError) as e:
#     print(e)
#
# except:
#     # handle all other exceptions
#     print('Nie mam pojęcia jakim jestem błędem')
#
# except Exception:
#   print("Nie mam pojęcia jaki błąd może mi się przydażyć")
#
# except Exception as e:
#     pass
#
# try:
#     x = float(input("podaj liczbę: "))
#     result = 5 / x
# except ZeroDivisionError as e:
#     print("Nie dziel przez zero! Twój wyjątek to:", e)
#     x = 1 # potrzebujemy x więc go nadpiszemy
# finally:
#     print ("Zawsze się wyświetlę")
#
# print(x + 4)
# niezbyt ładna wersja tego jak sprawdzić klasę błędu
# import sys
# try:
#     dict = {'phone':'samsung', 'speakers':'denon'}
#     print = dict[1]
# except Exception as e:
#     print("Błąd to: ", type(e))
#
# druga ładna wersja
# import sys
#
# try:
#     dict = {'phone':'samsung', 'speakers':'denon'}
#     print = dict[1]
# except Exception as e:
#     print("Błąd to: ", sys.exc_info()[0])
# raise ValueError('Whaaatever!')
# przykład zadania z funkcją która ma wywołać błąd:

import sys

def hello_exception():
    print("początek programu")
    raise ArithmeticError('To jest błąd arytmetyczny')
    print('Koniec programu')

try:
    hello_exception()
except ArithmeticError as ex:
    print('oh nie, błąd!', ex)
    print(sys.exc_info())
except:
    print('Inny błąd')
