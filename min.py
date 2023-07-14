def find_smallest_subarray_size(A):
    maximum = max(A)
    minimum = min(A)

    start = 0
    end = 0
    for i in range(len(A)):
        if A[i] == maximum:
            start = i
            end = i
            break
        elif A[i] == minimum:
            start = i
            end = i
            break

    min_max_size = end - start + 1
    for i in range(end + 1, len(A)):
        if A[i] == maximum or A[i] == minimum:
            end = i
            min_max_size = min(min_max_size, end - start + 1)

    return min_max_size
