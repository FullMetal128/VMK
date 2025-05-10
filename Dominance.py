import math


def calculate_dominance(arr):
    # Проверка, что массив не пустой
    if not arr:
        return "Массив пустой"

    # Проверка, что массив содержит только 0 и 1
    if not all(x in [0, 1] for x in arr):
        return "Массив должен содержать только 0 и 1"

    # Проверка, что длина массива — степень двойки
    length = len(arr)
    if not (length and (length & (length - 1) == 0)):
        return "Длина массива должна быть степенью двойки (2^n)"

    # Вычисление n (количество переменных)
    n = int(math.log2(length))

    # Подсчет веса функции (количество единиц)
    weight = arr.count(1)

    # Вычисление преобладания по формуле: δ(f) = 1 - ||f|| / 2^(n-1)
    dominance = 1 - weight / (2 ** (n - 1))

    # Формирование результата
    zeros = length - weight
    result = {
        'n': n,
        'weight': weight,
        'zeros': zeros,
        'dominance': dominance,
        'interpretation': (
            "Нули преобладают" if dominance > 0 else
            "Единицы преобладают" if dominance < 0 else
            "Нули и единицы сбалансированы"
        )
    }

    return result
