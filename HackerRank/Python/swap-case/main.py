def swap_case(s):
    return "".join([letter.lower() if letter == letter.upper() else letter.upper() for letter in list(s)])


if __name__ == "__main__":
    string = 'HackerRank.com presents "Pythonist 2"'
    print(swap_case(string))
