class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A < 2: return A
        
        low, high = 1, A + 1
        
        while high - low > 1:
            mid = low + (high - low)//2
            
            if mid * mid <= A:
                low = mid
            else:
                high = mid
                
        return low