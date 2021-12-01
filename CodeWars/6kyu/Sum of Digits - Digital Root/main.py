# My Method 1~ 🦉
def digital_root(n):
    def sum_elements(number):
        return sum([int(num) for num in str(number)])

    sum_final = sum_elements(n)
    while sum_final > 9:
        sum_final = sum_elements(sum_final)

    return sum_final


test_case = digital_root(493193)
print(test_case)
