class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        '''
        1, 1, 2, 2, 3, 4, 4,
        0, 1, 2, 3, 4, 5, 6
        
        '''
        len_a = len(A)
        
        if len_a == 1: return A[0]
        if A[0] != A[1]: return A[0]
        if A[len_a - 1] != A[len_a - 2]: return A[len_a - 1]
        
        start, end = 1, len_a - 2
        
        while start <= end:
            mid = start + (end - start)//2
            
            if A[mid] != A[mid + 1] and A[mid] != A[mid - 1]: return A[mid]
            
            if mid % 2 == 0:
                if A[mid] == A[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if A[mid] == A[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
                