from itertools import product

def eval_zhegalkin(coeffs, x):
    result = 0
    for i in range(8):
        bits = [(i >> 2) & 1, (i >> 1) & 1, i & 1]
        term = 1
        for j in range(3):
            if bits[j] == 1:
                term &= x[j]
        result ^= coeffs[i] * term
    return result

def is_fictive_variable(coeffs, var_index):
    for x in product([0, 1], repeat=3):
        x1 = list(x)
        x2 = list(x)
        x2[var_index] ^= 1  # инвертируем переменную

        if eval_zhegalkin(coeffs, x1) != eval_zhegalkin(coeffs, x2):
            return False
    return True

def find_fictive_variables(coeffs):
    names = ['x2', 'x1', 'x0']
    if [names[i] for i in range(3) if is_fictive_variable(coeffs, i)] == []:
        return ['нету']
    else:
        return [names[i] for i in range(3) if is_fictive_variable(coeffs, i)]

