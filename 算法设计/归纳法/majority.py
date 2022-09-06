def candidate(A, i):

    c = A[i]
    count = 1
    j = i+1
    while count != 0:
        if c == A[j]:
            count += 1
        else:
            count -= 1

        j += 1
        if j == len(A):
            return c

    if j == len(A)-1:
        return A[-1]  # remains the last ele
    else:
        return candidate(A, j)


def majority(A):
    c = candidate(A, 0)
    count = 0
    for ele in A:
        if ele == c:
            count += 1
    return c if (count > len(A)//2) else None


testcases = [[1, 2, 3, 3, 3], [1, 1, 1, 3], [1, 2, 3, 3],
             [1, 1], [1, 2, 1, 1], [1, 2, 1, 2], [1, 3, 2, 3, 3]]
for A in testcases:
    print(majority(A))
