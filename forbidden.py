import math
from itertools import product, combinations


def check_forbidden_sequences(arr, max_l=None):
    """
    Проверяет, является ли булева функция без запретов, и строит множество запретов.
    arr: массив значений функции (длина 2^n, содержит 0 и 1).
    max_l: максимальная длина последовательности y для проверки (по умолчанию 2^n).
    """
    # Проверка корректности
    if not arr:
        return "Массив пустой", []
    if not all(x in [0, 1] for x in arr):
        return "Массив должен содержать только 0 и 1", []

    length = len(arr)
    if not (length and (length & (length - 1) == 0)):
        return "Длина массива должна быть степенью двойки (2^n)", []

    n = int(math.log2(length))
    max_l = min(max_l or length, length)  # Ограничиваем l

    # Подсчет нулей и единиц
    weight = arr.count(1)
    zeros = length - weight
    dominance = 1 - weight / (2 ** (n - 1))

    # Индексы входов для 0 и 1
    zeros_indices = [i for i, v in enumerate(arr) if v == 0]
    ones_indices = [i for i, v in enumerate(arr) if v == 1]

    forbidden = []

    # Проверка для каждого l
    for l in range(1, max_l + 1):
        # Перебор всех последовательностей y^1, ..., y^l
        for y in product([0, 1], repeat=l):
            # Проверяем, есть ли решение для системы f(x^t) = y^t
            # Подсчитываем, сколько y^t равно 0 и 1
            y_zeros = y.count(0)
            y_ones = y.count(1)

            # Если нужно больше нулей или единиц, чем есть в массиве, это запрет
            if y_zeros > len(zeros_indices) or y_ones > len(ones_indices):
                forbidden.append(y)
                continue

            # Проверяем, можно ли выбрать l различных входов
            # Для простоты проверяем комбинации
            has_solution = False
            for comb in combinations(range(length), l):
                valid = True
                for t, idx in enumerate(comb):
                    if arr[idx] != y[t]:
                        valid = False
                        break
                if valid:
                    has_solution = True
                    break

            if not has_solution:
                forbidden.append(y)

    result = {
        'array': arr,
        'n': n,
        'weight': weight,
        'zeros': zeros,
        'dominance': dominance,
        'forbidden': forbidden,
        'is_without_forbidden': len(forbidden) == 0
    }

    return result['forbidden']