def PalindromicSubstring(strParam):

    # code goes here
    word_list = []
    for letter in strParam:
        listaA = strParam.split(letter)
        listaB = strParam[::-1].split(letter)

        for word in listaA:
            if word in listaB and len(word) > 2:
                word_list.append(f"{letter}{word}{letter}")

    result = max(word_list) if len(word_list) > 0 else "none"
    return result


# keep this function call here
print(PalindromicSubstring("abcdefgg"))
