from typing import List, Tuple


def min_max(*numbers: List[int]) -> Tuple[int, int]:
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    return min, max


print(min_max(1, 2, 3, 4))
