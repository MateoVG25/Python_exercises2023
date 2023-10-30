def int_number(message):
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            else:
                print("Por favor, ingrese un numero")
        except ValueError:
            print("Por favor, ingrese un numero")

def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    element = int(input(f"Ingrese el elemento para la row {i+1} y columna {j+1}: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Por favor, ingrese un numero")
        matrix.append(row)
    return matrix

def arrays_sum(arrays):
    rows = len(arrays[0])
    columns = len(arrays[0][0])
    matrix_result = [[0] * columns for _ in range(rows)]
    for matrix in arrays:
        for i in range(rows):
            for j in range(columns):
                matrix_result[i][j] += matrix[i][j]
    return matrix_result

arrays_number = int_number("Ingrese la cantidad de arrays a sumar: ")
rows = int_number("Ingrese la cantidad de filas: ")
columns = int_number("Ingrese la cantidad de columnas: ")

arrays = []
for _ in range(arrays_number):
    matrix = create_matrix(rows, columns)
    arrays.append(matrix)

matrix_result = arrays_sum(arrays)

print("Matrices ingresadas:")
for i, matrix in enumerate(arrays):
    print(f"Matriz {i+1}:")
    for row in matrix:
        print(row)
    print()

print("Matriz resultante:")
for row in matrix_result:
    print(row)