def denseMatrix(m: int, n: int):
    toReturn = {}
    counter = 0
    for i in range(m):
        for j in range(n):
            toReturn[(i, j)] = counter
            counter += 1
    return toReturn

print(denseMatrix(2, 4))