if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    lista = list(filter((max(arr)).__ne__, arr))
    print(max(lista))


# A função filter() assume outra função, __ne__, que retornará um bool True ou False com base no fato
# de o valor max(arr) estar presente na lista arr ou não.
