def timer():
    def sort_elements(sort_metod):
        start
        sort_method()
        end
        return end - start
    return sort_elements

#  sorting methods
@timer
def quicksort():
    pass
@timer
def countingsort():
    pass
@timer
def bubblesort():
    pass

clock = timer()

result_of_bubblesort = clock(bubblesort)

#  ALE nie trzeba 2 wy�ej linijek, jak dodamy @timer linijk� wy�ej, wywo�anie quicksorta zawsze wywo�a timer i zwr�ci ich czas

