# My Method 1~ 🦉
import math
def persistence(n):
    n_string = str(n)
    count = 0
    while len(n_string) > 1:
        n_string = str(math.prod(map(int, list(n_string))))
        count += 1
    return count


test_case = 999
print(persistence(test_case))
