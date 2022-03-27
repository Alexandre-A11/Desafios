def split_and_join(line):
    # write your code here
    return "-".join(line.split())


if __name__ == "__main__":
    string = "this is a string"
    print(split_and_join(string))
