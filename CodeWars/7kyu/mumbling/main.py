# My Method 1~ 🦉
def accum(s):
    return "-".join([(letter * i).title() for i, letter in enumerate(s, 1)])


test_cases = ["abcd", "RqaEzty", "cwAt"]

for test in test_cases:
    test_case = accum(test)
    print(test_case)
