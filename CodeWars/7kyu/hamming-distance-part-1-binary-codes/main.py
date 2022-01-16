def hamming_distance(a, b):
    count = 0
    for i, v in enumerate(a):
        if a[i] != b[i]:
            count += 1
    return count


print(hamming_distance("100101", "101001"))
print(hamming_distance("1010", "0101"))
