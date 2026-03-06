pi = 3.14159
print(f"pi = {pi}")
print(f"{pi = }")

n = 1234567.89123

print(f"{n = :.2f}")
print(f"{n = :.0f}")
print(f"{n = :,.2f}")
print(f"{n = :_.2f}")
print(f"{n = :.2e}")
print(f"{n = :+,.2f}")

progress = 0.4333
print(f"{progress = :.2%}")
print(f"{progress = :.0%}")

width = 10
dec = 3
print(f"{pi = :{width}.{dec}f}")

text = "Pls follow"
print(f"{text = :<30}")
print(f"{text = :->30}")
print(f"{text = :*^30}")
