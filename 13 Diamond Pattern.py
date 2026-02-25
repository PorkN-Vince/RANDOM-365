rows =5

#Upper half
for level in range(1, rows + 1):
    print(" " * (rows - level) + "*" * (2 * level - 1))

#Lower half
for level in range(rows - 1, 0, -1):
    print(" " * (rows - level) + "*" * (2 * level - 1))