def findMinXor(A):
    A.sort()
    minXor = A[1] ^ A[0]
    for i in range(2, len(A)):
        minXor = min(minXor, A[i] ^ A[i - 1])
        
    return minXor