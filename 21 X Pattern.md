import math

def draw_pattern():
    a = math.tan(math.pi * 0.4)
    b = math.tan(math.pi * 0.2)

    size = float(input("Enter the size:\n"))

    for y in range(math.ceil(size * a), -1, -1):
        for x in range(-math.ceil(0.55 * size * a / b), math.ceil(0.55 * size * a / b)):
            if ((y <= 0.55 * size * a and y >= (-x) * b and y >= x * b) or (y > 0.55 * size * a and y <= (size - x) * b and y <= (size + x) * b)):
                print("*", end="")
            else:
                print(" ", end="")
                print()

if __name__ == "__main__":
    draw_pattern()
