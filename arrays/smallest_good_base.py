def findSummation(x, p):
    sm, pw = 1, x
    for i in range(1, p + 1):
        sm += pw
        pw *= x
        
    return sm

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        '''
        1 + x + x^2 + ... + x^p = A
        
        '''
        
        n = int(A)
        for p in range(63, 0, -1):
            
            low, high = 2, n - 1
            
            while low <= high:
                mid = low + (high - low)//2
                
                sm = findSummation(mid, p)
                if sm == n:
                    return str(mid)
                elif sm > n:
                    high = mid - 1
                else:
                    low = mid + 1