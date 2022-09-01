# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort()
    target = sum(arr) // 2
    # We start with A=[arr[-1]] and expand to the left
    # Instead of keeping a list, we save space and time by only tracking the index
    i = len(arr) - 2  # 2 because A contains at least the last element
    sum_A = sum(arr[i:])

    while sum_A <= target:
        # Optimization: Get the remaining sum and divide by the max numbers that can be to the left
        min_steps = max(1, (target - sum_A) // max(1, arr[i]))
        # instead of calculating the sum over all elements in A, only add the new part
        sum_A += sum(arr[i-min_steps:i])
        i -= min_steps

    return arr[i:]



teste = minimalHeaviestSetA([4,2,5,1,6])
print(teste)

