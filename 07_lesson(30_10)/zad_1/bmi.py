def bmi_calculator(weight, height):
    return round(weight/(height ** 2), 3)


def bmi_status(bmi):
    if bmi < 16:
        return "severely_underweight"
    elif bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    elif bmi < 30:
        return "overweight"
    else:
        return "severely_overweight"


def main():
    print("***************")
    result = bmi_calculator(56, 1.75)
    print(bmi_status(result))
    print("***************")


if __name__ == "__main__":
    main()