'''
This problem does not clarify how uniqueness among pairs works
solve([2, 2, 2, 2, 2], 4) is supposed to give 4, but why?
'''

from collections import Counter

def solve(A, B):
    remainders = [0] * B
    for x in A:
        remainders[x%B] += 1
    
    p, q, pairs =  1, B - 1, 0
    pairs += (remainders[0] * (remainders[0] - 1)) // 2
    
    while p <= q:
        if p == q:
            # divide by 2 to remove duplicates
            pairs += (remainders[p] * (remainders[p] - 1)) // 2
        else:
            # no duplicate pairs for distinct numbers
            pairs += (remainders[p] * remainders[q])
            
        p += 1
        q -= 1
            
    return pairs % int(1e9 + 7)

print(solve([1, 2, 3, 4, 5], 2))