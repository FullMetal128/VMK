import gen_per
import get_coordinate_functions_vector
import coord
import jega
import fictive
import Dominance
import equiprobability
import forbidden

per = gen_per.bbs_shuffle_v6()

print("Подстановка на основе BBS:", per)
print(' ')

s0, s1, s2 = get_coordinate_functions_vector.get_coordinate_functions_vector(per)

print("Подстановка S(x):", per)
print("s₀(x) (младший бит):", s0)
print("s₁(x):", s1)
print("s₂(x) (старший бит):", s2)
print(' ')


print("s₀(x):", s0, "→ вес =", coord.hamming_weight(s0))
print("s₁(x):", s1, "→ вес =", coord.hamming_weight(s1))
print("s₂(x):", s2, "→ вес =", coord.hamming_weight(s2))
print(' ')

#Жегалкин
# Дополняем нулями до длины 8 (вместо фиктивных S(6), S(7))
s0 += [0, 0]
s1 += [0, 0]
s2 += [0, 0]


print("Полином Жегалкина для s₀(x):", jega.build_zhegalkin_polynomial(s0))
print("Полином Жегалкина для s₁(x):", jega.build_zhegalkin_polynomial(s1))
print("Полином Жегалкина для s₂(x):", jega.build_zhegalkin_polynomial(s2))
print(' ')

print(s0)

print("Фиктивные переменные для s₀(x):", fictive.find_fictive_variables(jega.zhegalkin_coefficients(s0)))
print("Фиктивные переменные для s₁(x):", fictive.find_fictive_variables(jega.zhegalkin_coefficients(s1)))
print("Фиктивные переменные для s₂(x):", fictive.find_fictive_variables(jega.zhegalkin_coefficients(s2)))
print(' ')

#LAB2-----------------------------------------------------------------------------------------------------

print(f'Преобладание нулей над единицами: {Dominance.calculate_dominance(s0)['dominance']}')
print(f'Преобладание нулей над единицами: {Dominance.calculate_dominance(s1)['dominance']}')
print(f'Преобладание нулей над единицами: {Dominance.calculate_dominance(s2)['dominance']}')
print(' ')

print(f'Функция {equiprobability.is_strongly_balanced(s0)}')
print(f'Функция {equiprobability.is_strongly_balanced(s1)}')
print(f'Функция {equiprobability.is_strongly_balanced(s2)}')
print(' ')

print(f'{forbidden.check_forbidden_sequences(s0)}')
print(f'{forbidden.check_forbidden_sequences(s1)}')
print(f'{forbidden.check_forbidden_sequences(s2)}')