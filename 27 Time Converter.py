def time_converter(value, unit):
    if unit == "sec_to_min":
        return value / 60
    elif unit == "min_to_sec":
        return value * 60
    elif unit == "min_to_hr":
        return value / 60
    elif unit == "hr_to_min":
        return value * 60
    else:
        return "Invalid choice"

#Main Program

if __name__ == "__main__":
    print("Convertion Options:")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")

    choice = int(input("Enter your choice (1-4): "))
    value = float(input("Enter the value to convert: "))

    #Set convertion unit based on user choice
    if choice == 1:
        unit = "sec_to_min"
        target = "minutes"
    elif choice == 2:
        unit = "min_to_sec"
        target = "seconds"
    elif choice == 3:
        unit = "min_to_hr"
        target = "hours"
    elif choice == 4:
        unit = "hr_to_min"
        target = "minutes"
    else:
        print("Invalid choice")
        exit()


    print(f"Converted Time: {time_converter(value, unit)} {target}")