# Método 1
# def divisors(integer):
#     array = []
#     for i in range(1, integer+1):
#         if integer % i == 0:
#             array.append(i)
#     if len(array) == 2:
#         return f"{integer} is prime"
#     else:
#         remove_these = [1, integer]
#         for i in remove_these:
#             array.remove(i)
#         return array

# Método 2
def divisors(integer):
    lista = [i for i in range(2, integer) if integer % i == 0]
    if len(lista) == 0:
        return f"{integer} is prime"
    return lista


print(divisors(25))

# the remove() function can be used on any array in Python.
