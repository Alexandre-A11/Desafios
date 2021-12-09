def in_array(array1, array2):
    # your code
    resultado = []
    for palavra_lista_1 in array1:
        for palavra_lista_2 in array2:
            if palavra_lista_1 in palavra_lista_2 and palavra_lista_1 not in resultado:
                resultado.append(palavra_lista_1)
    return sorted(resultado)