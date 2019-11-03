print("Body Mass Index - BMI calculator")
print()

def bmi_calculator(weight, height):
    return round((weight / height**2), 2)


def bmi_status(bmi):
    if bmi < 18.49:
        print('Your BMI is:', bmi, "- underweight.")
    elif bmi < 24.99:
        print('Your BMI is:', bmi, "- normal (healthy) weight.")
    elif bmi < 29.99:
        print('Your BMI is:', bmi, "- overweight.")
    else:
        print('Your BMI is:', bmi, "- obesity.")

def main():
    result = bmi_calculator(56, 1.6)
    bmi_status(result)

if __name__ == "__main__":
    main()
