texto = input("informe um texto:")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
       print (letras, end="")
       
print ()