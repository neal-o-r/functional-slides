from typing import List

Vector = List[int]

def scale(lst: Vector, s: int=5) -> Vector:
    return [s * v for v in lst]

scale(['1', '2', '3', '4'])

