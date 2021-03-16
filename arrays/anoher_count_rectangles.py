def solve(A, B):
    i, j = 0, len(A) - 1
    pairs = 0
    
    while i <= j:
        if A[i] * A[j] < B:
            pairs += (2 * (j - i + 1) - 1)
            i += 1
        else:
            j -= 1

    return pairs % int(1e9 + 7)