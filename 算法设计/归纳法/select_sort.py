def find_max(A, i):
    j = i
    for k in range(0, len(A[i:])):
        if A[i+k] > A[j]:
            j = i+k
    return j


def select_sort(A, i):

    if i < len(A):
        j = find_max(A, i)
        if j != i:
            A[i], A[j] = A[j], A[i]
        select_sort(A, i+1)


A = [1, 2, 3, 2, 1, 3]
select_sort(A, 0)
print(A)
