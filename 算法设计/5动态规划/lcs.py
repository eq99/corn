def lcs(A, B):
    n = len(A)
    m = len(B)

    L = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:  # A[i-1], B[i-1]: fix index from 0
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])

    return L[n][m]


A = "zxyxyz"
B = "xyyzx"

print(lcs(A, B))
