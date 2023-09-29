string = input("Ingrese una string de caracteres: ")
inversed_string = ""

for i in range(len(string) - 1, -1, -1):
    inversed_string += string[i]

print("Cadena invertida:", inversed_string)