# My Method 1~ 🦉
def descending_order(num):
    # return int("".join(map(str, list(reversed(sorted(list(map(int, list(str(num))))))))))
    return int("".join(sorted(str(num), reverse=True)))  # Alternative


tests_cases = [42145, 145263, 123456789]

for test in tests_cases:
    print(descending_order(test))

# TODO:
# 1) Converter elemento em String
# 2) Transformar String em Lista
# 3) Converter Elementos da Lista de String para Integer
# 4) Ordenar Lista
# 5) Reverter a Lista
# 6) Converter Elementos para String
# 7) Concatenar Lista
# 8) Converter para Integer
