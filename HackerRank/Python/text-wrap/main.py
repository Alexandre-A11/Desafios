def wrap(string, max_width):
    line = ""
    count = 0
    for letter in string:
        line += letter
        count += 1
        if count == max_width:
            count = 0
            line += "\n"
    return line


test = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)

print(test)
