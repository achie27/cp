class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        '''
        C = 3
        1, 2,    4,     8, 9
        1        2      3
        
        ans = 3 (4 - 1)
        '''
        
        A.sort()
        
        low = min([A[i] - A[i - 1] for i in range(1, len(A))]) # min possible
        high = A[len(A) - 1] - A[0] + 1 # can't ever be this
        
        while high - low > 1:
            mid = low + (high - low)//2
            
            prevPos = 0 # setting the first cow here
            i, cowsPositioned = 1, 1
            
            while i < len(A):
                if A[i] - A[prevPos] >= mid:
                    cowsPositioned += 1
                    prevPos = i
                
                i += 1
                
            if cowsPositioned >= B:
                low = mid
            else:
                high = mid
            
        return low