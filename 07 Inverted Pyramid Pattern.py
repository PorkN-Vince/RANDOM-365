rows =5
for level in range(rows, 0, -1):
    print(" " * (rows - level) + "*" * (2 * level -1))