def get_coordinate_functions_vector(S):
    coord_0 = []  # младший бит
    coord_1 = []  # средний бит
    coord_2 = []  # старший бит

    for val in S:
        bits = f'{val:03b}'  # двоичное представление
        coord_2.append(int(bits[0]))
        coord_1.append(int(bits[1]))
        coord_0.append(int(bits[2]))

    return coord_0, coord_1, coord_2

def hamming_weight(bits):
    return sum(bits)

