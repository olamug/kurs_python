# skopiowane z cmd
>>> a =7
>>> b=7
>>> a_to_float = float(a)
>>> a_to_float
7.0
>>> int(b)
7
>>> int(a)
7
>>> float(a)
7.0
>>> float(b)
7.0
>>> txt = '124'
>>> txt + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> num = int(txt)
>>> num
124
>>> num = float(txt)
>>> num
124.0
>>> txt
'124'
>>> num + 4
128.0
>>> txt = '124.345'
>>> txt + 4.3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
>>> num = float(txt)
>>> num + 4.3
128.645
>>> num = 6
>>> 'Ala ma ' + num + ' kotów'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print ('Ala ma ' + num + ' kotów')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> num = str(num)
>>> 'Ala ma ' + num + ' kotów'
'Ala ma 6 kotów'
>>> txt =str(num)
>>> 'Ala ma ' + txt + ' kotów'
'Ala ma 6 kotów'

# zapiski
Rzutowanie = konwersja (tekst na liczby, całkowite na dziesiętne itp)
Aby zobaczyć jaki to rodzaj zmiennych wpisujemy type ("hello") -<w nawiasie moja zmienna
Jakie są słowa klucze: help() -> keywords albo help("keywords")
Zen Python = wpisz import this