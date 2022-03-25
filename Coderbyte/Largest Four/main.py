def LargestFour(arr):

    # code goes here
    if len(arr) <= 4:
        return sum(arr)

    largest = []
    for _ in range(4):
        large_n = max(arr)
        arr.remove(large_n)
        largest.append(large_n)

    return sum(largest)


# keep this function call here
print(LargestFour([0, 0, 2, 3, 7, 1]))
