import math
from itertools import combinations


def is_strongly_balanced(arr, verbose=False):
    if not arr:
        return "Массив пустой", False
    if not all(x in [0, 1] for x in arr):
        return "Массив должен содержать только 0 и 1", False

    length = len(arr)
    is_power_of_2 = length and (length & (length - 1) == 0)

    if not is_power_of_2:
        return "Длина массива должна быть степенью двойки (2^n)", False

    n = int(math.log2(length))
    weight = arr.count(1)
    zeros = length - weight
    dominance = 1 - weight / (2 ** (n - 1))

    # Проверка для l=1 (сбалансированность)
    if weight != 2 ** (n - 1):
        return f"Функция не сбалансирована: единиц={weight}, ожидается {2 ** (n - 1)}", False

    # Проверка для l=2 (пример)
    zeros_indices = [i for i, v in enumerate(arr) if v == 0]
    ones_indices = [i for i, v in enumerate(arr) if v == 1]

    # Проверяем комбинации (y^1, y^2)
    solutions = {
        (0, 0): len(list(combinations(zeros_indices, 2))),
        (0, 1): sum(1 for x1 in zeros_indices for x2 in ones_indices if x1 != x2),
        (1, 0): sum(1 for x1 in ones_indices for x2 in zeros_indices if x1 != x2),
        (1, 1): len(list(combinations(ones_indices, 2)))
    }

    expected_solutions = 2 ** (n - 1)
    is_strongly_balanced = all(count == expected_solutions for count in solutions.values())

    result = {
        'array': arr,
        'n': n,
        'weight': weight,
        'zeros': zeros,
        'dominance': dominance,
        'solutions_l2': solutions if verbose else None,
        'interpretation': (
            "Функция сильно равновероятна" if is_strongly_balanced else
            "Функция не сильно равновероятна"
        )
    }

    return result, is_strongly_balanced


