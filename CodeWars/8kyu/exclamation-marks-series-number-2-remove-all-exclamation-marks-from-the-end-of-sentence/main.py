def remove(s):
    count = 0
    new_s = s
    for i in range(len(s)-1, 0, -1):
        if s[i] == "!":
            count += 1
            new_s = s[:-count]
        else:
            break
    return new_s


teste = "Hi! Hi!"
print(remove(teste))


# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# Example:
# def remove(s):
#     return s.rstrip("!")

# The replace() method replaces a specified phrase with another specified phrase.
# Example:
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)
