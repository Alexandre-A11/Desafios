def string_clean(s):
    s = list(s)
    for number in "0123456789":
        while number in s:
            s.remove(number)
    return "".join(s)


print(string_clean("! !"))
print(string_clean("123456789"))
print(string_clean("This looks5 great8!"))
print(string_clean("(E3at m2e2!!)"))
print(string_clean('My "me3ssy" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?'))
