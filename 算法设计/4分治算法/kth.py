def kth(A, k):
    a = A[0]
    A0 = []
    A1 = []
    A2 = []
    for ele in A:
        if ele < a:
            A1.append(ele)
        elif ele == a:
            A0.append(ele)
        else:
            A2.append(ele)

    if k <= len(A1):
        return kth(A1, k)
    elif k > len(A0)+len(A1):
        return kth(A2, k-len(A1)-len(A0))
    else:
        return a


testcases = [[1, 2, 3, 4, 5, 6], [1, 1, 1, 34, 5], [51, 76, 12, 34, 89, 42]]

for A in testcases:
    print(kth(A, 3))
