def grid_index(grid, indexes):
    matriz = []
    for list in grid:
        matriz += list

    word = ""
    for i in indexes:
        word += matriz[i - 1]

    return word


print(
    grid_index(
        [["h", "e", "l", "l"], ["o", "c", "o", "d"], ["e", "w", "a", "r"], ["r", "i", "o", "r"]],
        [5, 7, 9, 3, 6, 6, 8, 8, 16, 13],
    )
)

print(grid_index([["m", "y", "e"], ["x", "a", "m"], ["p", "l", "e"]], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
