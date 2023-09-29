number = int(input("Ingrese un número: "))

print("Tabla de multiplicar del", number)
for i in range(11):
    result = number * i
    print(number, "x", i, "=", result)