
import timeit
import operator
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

points = [Point(i, i * 2) for i in range(1_000_000)]

t = timeit.timeit(lambda: sorted(points, key=lambda p: p.y), number=10)
print(f"Lambda: {t:.4f}s")

t = timeit.timeit(lambda: sorted(points, key=operator.attrgetter("y")), number=10)
print(f"attrgetter:{t:.4f}s")