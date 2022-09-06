"""

def merge(A, B):
    C = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] >= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < len(A):
        C += A[i:]
    if j < len(B):
        C += B[j:]
    return C


A = [9, 7, 5, 3, 1]
B = [8, 6, 4, 2, 0]
C = merge(A, B)
print(C)
"""


def merge(A, low, mid, high):
    pass


def merge_sort(A, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(A, low, mid)
        merge_sort(A, mid+1, high)
        merge(A, low, mid, high)
