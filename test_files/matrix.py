def make_matrix(rows, cols):
    matrix = []
    for i in xrange(rows):
        row = []
        for j in xrange(cols):
            row.append(i * j)
        matrix.append(row)
    return matrix

m = make_matrix(3, 3)
print m
