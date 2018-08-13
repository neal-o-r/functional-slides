from typing import List

Vector = List[int]

def cumulative(lst: Vector) -> Vector:
    c = lst[0]
    out = [c]
    for item in lst[1:]:
        c += item
        out.append(c)

    return out

cumulative(['1', '2', '3', '4'])
