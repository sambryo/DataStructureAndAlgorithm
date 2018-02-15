def insertion_sort(A):
    for k in range(1, len(A)):
        curr = A[k]
        j = k
        while (0 < j) and (A[j - 1] > curr):
            A[j] = A[j - 1]
            j -= 1
        A[j] = curr
    return A


print(insertion_sort([4, 1, 3, 2, 0, 6, 5]))
