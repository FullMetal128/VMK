def get_coordinate_functions_vector(S):
    # S — список длины 6: [S(0), S(1), ..., S(5)]
    coord_0 = []  # младший бит (s0)
    coord_1 = []  # средний бит (s1)
    coord_2 = []  # старший бит (s2)

    for val in S:
        bits = f'{val:03b}'  # двоичное представление из 3 бит, например "101"
        coord_2.append(int(bits[0]))  # старший
        coord_1.append(int(bits[1]))  # средний
        coord_0.append(int(bits[2]))  # младший

    return coord_0, coord_1, coord_2



