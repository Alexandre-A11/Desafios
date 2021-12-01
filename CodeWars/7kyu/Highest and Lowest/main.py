# My Method 1~ 🦉
def high_and_low(numbers):
    list_numbers = list(map(int, numbers.split(" ")))
    return f"{max(list_numbers)} {min(list_numbers)}"


# Method 2:
def high_and_low_2(numbers):
    nums = list(map(int, numbers.split(" ")))
    return " ".join(map(str, (max(nums), min(nums))))


test_case = high_and_low_2("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(test_case)
