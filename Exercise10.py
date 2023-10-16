length = int(input("Ingresa el tamaño de la lista: "))
my_list = []

for i in range(length):
    element = int(input("Digita un numero entero: "))
    my_list.append(element)

print("Lista:", my_list)
print("Aqui esta la suma de todos los elementos:", sum(my_list))

