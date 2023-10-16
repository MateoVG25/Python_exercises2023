my_list = ["A", "B", "b", "c", "E", "E", "f"]
print(my_list)

my_list = [element.lower() for element in my_list]

delete_element = input("Introduce la letra que deseas eliminar de la lista ").lower()

while delete_element in my_list:
    my_list.remove(delete_element)

print("Esta es la lista despues de eliminar el elemento", my_list)