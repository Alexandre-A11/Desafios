# My Method 1~ 🦉
def duplicate_encode(word):
    l_word = word.lower()
    return "".join([")" if l_word.count(letter) > 1 else "(" for letter in l_word])


test_case = ["din", "recede", "Success", "(( @", "E( cI!ACXAU@fN"]
for test in test_case:
    print(duplicate_encode(test))
