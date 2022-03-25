def RunLength(strParam):

    # code goes here
    qtd = 1
    result = ""
    for index, letter in enumerate(strParam):
        if index == len(strParam) - 1:
            if letter == strParam[index - 1]:
                break
            else:
                result += f"{1}{letter}"
        else:
            if letter == strParam[index + 1]:
                qtd += 1
            else:
                result += f"{qtd}{letter}"
                qtd = 1

    return result


# keep this function call here
print(RunLength(input()))
