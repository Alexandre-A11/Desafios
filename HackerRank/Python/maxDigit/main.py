# Returna numeros de 4 digitos onde cada numero seja menor que max_digit e a soma sena igual a 21;
def maxDigit(num):
    for i in range(0, (num + 1)):
        for j in range(0, (num + 1)):
            for k in range(0, (num + 1)):
                for l in range(0, (num + 1)):
                    if (i + j + k + l) == 21:
                        print(f"{i}{j}{k}{l}")


if __name__ == "__main__":
    num = int(input())
    maxDigit(num)
