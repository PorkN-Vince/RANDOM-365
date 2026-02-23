
a = [21, -6, 26, 11, 1, 16]
b = [17, 26, 7, 21, -2, 12]

union = set(a) | set(b)
intersection = set(a) & set(b)
difference = set(a) - set(b)
symmetric_diff = set(a) ^ set(b)

print(f"{sorted(union)=}")
print(f"{sorted(intersection)=}")
print(f"{sorted(difference)=}") 
print(f"{sorted(symmetric_diff)=}")