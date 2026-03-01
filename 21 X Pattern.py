rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == j or j == rows + 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()