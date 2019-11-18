print("Body Mass Index - BMI calculator")
print()
weight = input("How much do you weight? ")
height = input("How tall are you? (Height in meters) ")
BMI = round((int(weight) / float(height)**2), 2)
if BMI < 18.49:
    print('Your BMI is:', BMI, "- underweight.")
elif BMI < 24.99:
    print('Your BMI is:', BMI, "- normal (healthy) weight.")
elif BMI < 29.99:
    print('Your BMI is:', BMI, "- overweight.")
else:
    print('Your BMI is:', BMI, "- obesity.")