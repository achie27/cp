import math

def solve(A):
    mx = max(A)
    spf = [-1] * (mx + 1)
    
    for i in range(2, int(math.ceil(math.sqrt(mx) + 1))):
        if spf[i] == -1:
            for j in range(i*i, mx + 1, i):
                if spf[i] == -1:
                    spf[j] = i
                
    result = []
    for e in A:
        divs = 1
        while e > 1:
            pf, cnt = spf[e], 1
            
            while e > 1 and e % pf == 0:
                cnt += 1
                e //= pf
        
            divs *= cnt
        
        result.append(divs)

    return result

print(solve([2, 3, 4, 5]))