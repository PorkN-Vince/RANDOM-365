def currency_converter(amount, rate):
    return round(amount * rate, 2)


if __name__ == "__main__":
    print("Currency Converter")
    print('1. USD to EUR')
    print('2. USD to GBP')
    print('3. USD to JPY')
    choice = input("Choose an option (1-3): ")

    amount = float(input("Enter the amount in USD: "))

    #Set conversion rate based on user choice
    if choice == '1':
        rate = 0.92  # USD to EUR
        target = "EUR"
    elif choice == '2':
        rate = 0.81  # USD to GBP
        target = "GBP"
    elif choice == '3':
        rate = 134.50  # USD to JPY
        target = "JPY"
    else:
        print("Invalid choice.")
        exit()

    print(f"Converted Amount: {currency_converter(amount, rate)} {target}")