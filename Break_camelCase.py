def separar_camelCase(word):
    letras = [letra for letra in word]
    # letras = list(word)
    palavra = ""
    for i in range(len(letras)):
        if letras[i] == letras[i].upper():
            palavra += " " + letras[i]
        else:
            palavra += letras[i]
    return palavra


palavra_coladas = "vamosSepararEssasPalavrasParaNuncaMaisErrar"

print(separar_camelCase(palavra_coladas))

import re

regex = re.sub("([A-Z])", r" \1", palavra_coladas)

print(regex)

# resultado = re.findall("[A-Z]+[a-z]+", palavra_coladas)
# print(resultado)
