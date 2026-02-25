rows = 5

#Top section
for level in range(1, rows + 1):
    print("*" * level + " " * (2 * (rows - level)) + "*" * level)

#Bottom section
for level in range(rows - 1, 0, -1):
    print("*" * level + " " * (2 * (rows - level)) + "*" * level)   