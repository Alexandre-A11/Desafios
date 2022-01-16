def reverse_sentence(sentence):
    return " ".join([word[::-1] for word in sentence.split()])

print(reverse_sentence("Hello !Nhoj Want to have lunch?"))