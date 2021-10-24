def knapsack(U, V, c):
    n = len(U)

    Result = [[0 for i in range(c+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, c+1):
            Result[i][j] = Result[i-1][j]
            if U[i-1] <= j:  # U[i-1]: fix index from 0, i.e. U[i]
                Result[i][j] = max(Result[i][j], Result[i-1][j-U[i-1]]+V[i-1]) # V[i-1]: fix index from 0

    return Result[n][c]


U = [2, 3, 4, 5]
V = [3, 4, 5, 7]
c = 9

print(knapsack(U, V, c))
