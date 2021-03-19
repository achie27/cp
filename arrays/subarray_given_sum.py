def solve(A, B):
    start, end, subarraySum, arrayLen = 0, 0, A[0], len(A)
    
    while end < arrayLen and start <= end:
        if subarraySum > B:
            subarraySum -= A[start]
            start += 1
        elif subarraySum < B:
            end += 1
            if end < arrayLen:
                subarraySum += A[end]
        else:
            return A[start: end + 1]
            
    
    return [-1]