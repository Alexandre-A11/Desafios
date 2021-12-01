# My Method 1~ 🦉
def find_it(seq):
    for element in seq:
        if seq.count(element) % 2 != 0:
            odd = element
    return odd


# Method 2:
def find_it_2(seq):
    return [element for element in seq if seq.count(element) % 2][0]


# False == 0
# True == 1
test_case = find_it_2([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])
print(test_case)
