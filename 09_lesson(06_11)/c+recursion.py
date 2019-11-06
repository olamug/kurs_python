def recur_function(n):
    if n < 0:
        n = -n
    if n / 10 != 0:
        recur_function(n/10)
        print("liczba", n % 10)

recur_function(123)