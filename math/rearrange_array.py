def solve(A):
    N = len(A)
    A = [(e + 1) * N for e in A]

    for i in range(N):
        oldValue = A[i] // N - 1
        A[oldValue] += i

    return [x%N for x in A]

print(solve([1, 2, 3, 4, 0]))