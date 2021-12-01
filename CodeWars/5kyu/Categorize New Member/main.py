# Minha solução
def open_or_senior(data):
    result = []
    for member in data:
        age = member[0]
        handicap = member[1]
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result


# Solução alternativa
def solution(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


################################################# Testes #####################################
teste = [(45, 12), (55, 21), (19, -2), (104, 20)]

chamar_func = open_or_senior(teste)
print(chamar_func)
