# Minha solução
def rgb(r, g, b):
    # a = (num // 16) // 16  # 1
    decimais = [r, g, b]
    resultado = ""
    for num in decimais:
        if num < 0:
            num = 0
        elif num > 255:
            num = 255
        resto_2 = (num // 16) % 16  # 11
        resto_1 = num % 16  # 6
        decimal = [resto_2, resto_1]
        for i in range(len(decimal)):
            if decimal[i] > 9 and decimal[i] < 16:
                if decimal[i] == 10:
                    decimal[i] = "A"
                elif decimal[i] == 11:
                    decimal[i] = "B"
                elif decimal[i] == 12:
                    decimal[i] = "C"
                elif decimal[i] == 13:
                    decimal[i] = "D"
                elif decimal[i] == 14:
                    decimal[i] = "E"
                else:
                    decimal[i] = "F"

        hexadecimal = [str(x) for x in decimal]
        converter_string = "".join(hexadecimal)
        resultado += converter_string
    return resultado


cor = [-100, 000, 000]

print(rgb(cor[0], cor[1], cor[2]))
