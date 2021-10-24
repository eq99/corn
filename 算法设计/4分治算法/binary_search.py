def binary_search(A, low, high, x):
    if low > high:
        return -1

    mid = (low+high)//2

    if x == A[mid]:
        return mid

    elif x < A[mid]:
        return binary_search(A, mid+1, high, x)

    else:
        return binary_search(A, low, mid-1, x)


A = [90, 87, 42, 30, 15, 5]

print(binary_search(A, 0, len(A)-1, 90))
print(binary_search(A, 0, len(A)-1, 42))
print(binary_search(A, 0, len(A)-1, 5))
print(binary_search(A, 0, len(A)-1, 1))
