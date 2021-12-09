# My Method 1~ 🦉
def square_digits(num):
    return int("".join(([str(int(number) ** 2) for number in str(num)])))


test_case = square_digits(9119)
print(test_case)
