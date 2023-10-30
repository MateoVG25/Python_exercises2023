def create_matrix(rows, columnas):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def show_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

rows = int(input("Ingrese la cantidad de filas de la matriz: "))
columns = int(input("Ingrese la cantidad de columnas de la matriz: "))

matrix = create_matrix(rows, columns)

print("Matriz resultante:")
show_matrix(matrix)