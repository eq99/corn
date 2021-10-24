from random import randint


def split(A, low, high):
    i = low
    x = A[low]
    for j in range(low+1, high+1):
        if A[j] >= x:
            i += 1
            if i != j:
                A[i], A[j] = A[j], A[i]

    A[i], A[low] = A[low], A[i]
    return i


def qsort(A, low, high):
    if low < high:
        mid = split(A, low, high)
        qsort(A, low, mid-1)
        qsort(A, mid+1, high)


A = [randint(0, 100) for i in range(0, 7)]
print(A)
qsort(A, 0, len(A)-1)
print(A)
