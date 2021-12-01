import string


def rot13(message):
    palavra = list(message)
    alfabeto = list(string.ascii_uppercase)
    palavra_codificada = ""

    for letra in palavra:
        # try verifica se a "letra" existe na lista "alfabeto"
        # caso negativo adiciona a letra não existente e pula para o proximo loop
        try:
            index = alfabeto.index(letra.upper())
        except ValueError:
            palavra_codificada += letra
            continue
        cod = index + 13
        if cod > 25:
            cod = cod % 13

        if letra == letra.upper():
            palavra_codificada += alfabeto[cod].upper()
        else:
            palavra_codificada += alfabeto[cod].lower()

    return "".join(palavra_codificada)


print(rot13("asEW"))