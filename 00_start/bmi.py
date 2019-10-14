print("Body Mass Index - BMI calculator")
print()
weight = input("How much do you weight? ")
height = input("How tall are you? ")
BMI = int(weight) / float(height)**2
print('Your BMI is:', round(BMI, 2))