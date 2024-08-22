def get_matrix(n, m, value):
    matrix = []
    n = int(n)
    m = int(m)
    for i in range(0, m):
        matrix.append(value)
    print([matrix] * n)

get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
get_matrix(6, 3, 77)
