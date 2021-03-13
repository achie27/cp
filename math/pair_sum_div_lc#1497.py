def canArrange(arr: List[int], k: int) -> bool:
    remainders = [0] * k
    for x in arr:
        remainders[x % k] += 1
    
    pairs = remainders[0] % 2 == 0
    p, q = 1, k - 1

    while p <= q:
        if p == q:
            pairs &= remainders[p] % 2 == 0
        else:
            pairs &= remainders[p] == remainders[q]
            
        p += 1
        q -= 1
        
    return pairs

print(canArrange([2, 2, 2, 2], 4))