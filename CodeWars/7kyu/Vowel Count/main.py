# My Method
def get_count(sentence):
    vogais = ["a", "e", "i", "o", "u"]
    count = 0
    for letra in vogais:
        count += sentence.count(letra)

    return count


# Method 2:
def get_count_2(sentence):
    return sum(1 for letra in sentence if letra in "aeiou")


# Method 3:
def get_count_3(sentence):
    # A boolean can be treated by Python as an integer value: 1 for True, 0 for False. 😲
    return sum(letra in "aeiou" for letra in sentence)


test_case = get_count("valorant")
test_case_2 = get_count_2("valorant")
test_case_3 = get_count_3("valorant")

print(test_case)
print(test_case_2)
print(test_case_3)
