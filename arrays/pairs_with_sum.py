import math

def solve(A, B):

    i, j = 0, len(A) - 1
    
    pairs = 0
    while j > i:
        if A[i] + A[j] > B:
            j -= 1
        elif A[i] + A[j] < B:
            i += 1
        else:
            last_i, last_j = i, j
            while j > i and A[last_i] == A[i + 1]:
                i += 1
                
            while j > i and A[last_j] == A[j - 1]:
                j -= 1
            
            # same digits from last_i to j/i
            if i == j:
                pairs += (math.factorial(i - last_i + 1) // (2 * math.factorial(i - last_i - 1)))
            else:
                pairs += ((last_j - j + 1) * (i - last_i + 1))
                
            i += 1
            j -= 1
            
    return pairs