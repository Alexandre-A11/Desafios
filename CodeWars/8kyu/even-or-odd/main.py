# My Method:
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

    ## * number % 2 will return 0 for even numbers and 1 for odd ones.
    ## 0 evaluates to False and 1 to True, so we can do it with one line
    return "Even" if not number % 2 else "Odd"  # Variations 1:
    return "Odd" if number % 2 else "Even"  # Variation 2:


# Method 2:
def even_or_odd_2(number):
    return ["Even", "Odd"][number % 2]


test_case = even_or_odd(10)
test_case_2 = even_or_odd_2(10)
print(test_case)
print(test_case_2)
