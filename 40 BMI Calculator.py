#convert feet to meters
def feet_to_meter(feet):
    return feet * 0.3048

#Calculate BMI
def bmi(weight, height_feet):
    return round(weight / (feet_to_meter (height_feet) **2), 2)

if __name__ == "__main__":
    weight = float(input("Weight (kg): "))
    height = float(input("Height (ft): "))

    BMI = bmi(weight, height)
    print("Your BMI is: ", BMI)
    