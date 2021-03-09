def gcdFunc(a, b):
    if b == 0:
        return a
    
    return gcdFunc(b, a%b)    

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        gcd = A[0]
        for e in A:
            gcd = gcdFunc(e, gcd)
            
        if gcd > 1: return 0
        else: return 1