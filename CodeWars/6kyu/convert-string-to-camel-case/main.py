import re


def to_camel_case(text):
    text_list = re.split("_|-", text)

    for i in range(len(text_list)):
        if i != 0:
            text_list[i] = text_list[i].title()
    text_again = "".join(text_list)
    return text_again


frase = "the_stealth_warrior"
almejado = "theStealthWarrior"

print(to_camel_case(frase))


# The split() method splits a string into a list.


# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
# import re

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string
