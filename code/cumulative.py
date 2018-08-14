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

def cumulative_recursive(lst: Vector) -> Vector:
    if len(lst) == 1:
        return lst
    return cumulative(lst[:-1]) + [sum(lst)]

cumulative_recursive([1, 2, 3, 4])
