class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        
        if len(A) == 1: return 0
        
        elems_with_index = [(x, i) for i, x in enumerate(A)]
        elems_with_index.sort()
        
        mx, ans, l = float('-inf'), float('-inf'), len(elems_with_index)
        
        for i in range(1, l):
            mx = max(elems_with_index[l - i][1], mx)
            ans = max(mx - elems_with_index[l - i - 1][1], ans)
            
        return ans if ans >= 0 else 0