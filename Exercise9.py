string = input("Ingrese una frase: ")
word = input("Ingrese un carácter: ")
no_vocals = ""
for Word in string:
  if Word in "aeiouAEIOU":
    continue
  if Word == word:
    break
  no_vocals += Word

print("La frase sin vocales es:", no_vocals)
