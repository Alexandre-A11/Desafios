# My Method 1~ 🦉
def duplicate_count(text):
    lower = list(text.lower())
    count = 0
    used_letters = ""
    for letter in lower:
        if lower.count(letter) > 1 and letter not in used_letters:
            count += 1
            used_letters += letter

    return count


# Method 2~ 🐉
def duplicate_count_2(string):
    return len([letter for letter in set(string.lower()) if string.lower().count(letter) > 1])


# Method 3~ 🐵
from collections import Counter


def duplicate_count_3(text):
    return sum(v > 1 for v in Counter(text.lower()).values())
    # Variation
    counter = Counter(text.lower())
    return len([counter.keys() for i in counter.values() if i > 1])


tests_list = [
    "abcde",
    "aabbcde",
    "aabBcde",
    "indivisibility",
    "Indivisibilities",
    "aA11",
    "ABBA",
    "DWJQ95X0yqXn5zZPQlM2jMIL",
]

# for test in tests_list:
#     print(duplicate_count_2(test))

print(duplicate_count_3("aabbcde"))
