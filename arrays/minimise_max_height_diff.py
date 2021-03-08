class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        
        diff = A[-1] - A[0]
        for i in range(len(A) - 1):
            min_height = min(A[0] + B, A[i + 1] - B)
            max_height = max(A[i] + B, A[-1] - B)
            diff = min(diff, max_height - min_height)
            
        return diff
