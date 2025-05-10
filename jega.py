from itertools import product



# Преобразование Жегалкина (обратное преобразование Мёбиуса)
def zhegalkin_coefficients(values):
    n = len(values)
    table = values.copy()
    coeffs = []
    for i in range(n):
        coeffs.append(table[0])
        table = [(table[j] ^ table[j+1]) for j in range(len(table) - 1)]
    return coeffs

# Получаем моном по номеру (x2, x1, x0)
def monomial(index):
    x_vars = ['x2', 'x1', 'x0']
    bits = f"{index:03b}"
    terms = [x_vars[i] for i in range(3) if bits[i] == '1']
    return '*'.join(terms) if terms else '1'

# Построение полинома Жегалкина
def build_zhegalkin_polynomial(values):
    coeffs = zhegalkin_coefficients(values)
    terms = [monomial(i) for i in range(len(coeffs)) if coeffs[i] == 1]
    return ' ⊕ '.join(terms)


