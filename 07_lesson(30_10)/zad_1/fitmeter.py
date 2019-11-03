import bmi


def main():
    w = float(input("How much do you weight? "))
    h = float(input("How tall are you? (Height in meters) "))
    bmi_result = bmi.bmi_calculator(w, h)
    bmi_status = bmi.bmi_status()
    print(bmi.bmi_calculator(60, 1.8))


if __name__ == '__main__':
    main()