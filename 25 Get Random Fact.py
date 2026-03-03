import randfacts

print("---- Infinite Fact Generator ----")

while True:
    input("Press Enter to get a random fact...")
    fact = randfacts.get_fact(filter_enabled=True)

    print("Did you know? " + fact)
    print("-" * 30)
        