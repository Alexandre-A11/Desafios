# My Method 1~ 🦉
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])


test_case = spin_words("This is another test")
print(test_case)


## Tests with reverse() and [::-1]
# [index:qtd:passo]
# list.reverse() # Work only with lists
lista = [5, 4, 3, 2, 1]
lista.reverse()
print(lista)

print(lista[::-1])

