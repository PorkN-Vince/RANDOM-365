# Convert Temperature
def temp_converter(value, scale):
    if scale == "CtoF":
        return (value * 9/5) + 32
    elif scale == "FtoC":
        return (value - 32) * 5/9
    elif scale == "CtoK":
        return value + 273.15
    elif scale == "KtoC":
        return value - 273.15
    else:
        return "Invalid scale. Use 'CtoF', 'FtoC', 'CtoK', or 'KtoC'."
    

#Main Program
if __name__ == "__main__":
    print("Conversion Options:")
    print("1. Celsius to Fahrenheit (CtoF)")
    print("2. Fahrenheit to Celsius (FtoC)")
    print("3. Celsius to Kelvin (CtoK)")
    print("4. Kelvin to Celsius (KtoC)")

    choice = input("Enter your choice (CtoF, FtoC, CtoK, KtoC): ")
    value = float(input("Enter the temperature value to convert: "))

#Set conversion scale based on user choice
    if choice == "1":
        scale = "CtoF"
        target = "Fahrenheit"
    elif choice == "2":
        scale = "FtoC"
        target = "Celsius"
    elif choice == "3":
        scale = "CtoK"
        target = "Kelvin"
    elif choice == "4":
        scale = "KtoC"
        target = "Celsius"
    else:
        print("Invalid choice. Please select a valid conversion option.")
        exit()
    
    print(f"Converted Temperature: {temp_converter(value, scale):.2f} {target}")