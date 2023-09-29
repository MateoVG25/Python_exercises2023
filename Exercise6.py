string = input("Ingrese la string de caracteres: ").lower()
word = input("Ingrese la word a eliminar: ").lower()

new_string = ""

words = string.split(" ") 

for string_word in words:
    if string_word != word:
        new_string += string_word + " "

print(new_string)