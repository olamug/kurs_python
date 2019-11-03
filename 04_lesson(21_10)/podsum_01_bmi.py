def calc_bmi(weight, height):
    return weight / height ** 2

def bmi_status(bmi):
    if bmi < 18.49:
        print('Your BMI is:', bmi, "- underweight.")
    elif bmi < 24.99:
        print('Your BMI is:', bmi, "- normal (healthy) weight.")
    elif bmi < 29.99:
        print('Your BMI is:', bmi, "- overweight.")
    else:
        print('Your BMI is:', bmi, "- obesity.")

weight = float(input("How much do you weight? "))
height = float(input("How tall are you? (Height in meters) "))

bmi = round(calc_bmi(weight, height), 2)
print(bmi)
bmi_status(bmi)
