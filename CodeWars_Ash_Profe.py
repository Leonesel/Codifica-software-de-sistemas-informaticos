def python_snake(xs):
    head = "H"
    tail = "T"
    body = "x"
    
    longitud = len(xs)
    columns = max(xs)
    matrix = []
    for i in range(longitud):
        row = []
        for x in range(columns):
            row.append('H')
            row.append('x')
            row.append('T')
            row.append(' ')

        matrix.append(row)
    return matrix 