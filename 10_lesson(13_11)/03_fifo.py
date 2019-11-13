class Fifo:

    def __init__(self, elements):
        self.elements = elements

    def show(self):
        print(self.elements)

    def __str__(self):
        return "-".join(self.elements) # wtedy print(fifol)

    def check(self):
        if len(self.elements) == 0:
            print("Kolejka jest pusta.")
        else:
            print("Twoja kolejka zawiera następujące elementy {}".format(self.elements))


    def put(self, value):
        return self.elements.append(value)

    def get(self):
        if len(self.elements) == 0:
            return "Pusta lista"
        else:
            return self.elements.pop(0)



list_elem = ["a", "b", "c", "d"]
fifo1 = Fifo(list_elem)

print(fifo1)
print(fifo1.get())
print(fifo1)
elem = input("Podaj co chcesz dodać do kolejki: ")
fifo1.put(elem)
print(fifo1)
fifo1.check()

