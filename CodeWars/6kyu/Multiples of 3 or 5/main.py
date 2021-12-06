def solution(number):
    return sum([i for i in range(3, number) if i % 3 == 0 or i % 5 == 0])


teste = solution(10)
print(teste)
