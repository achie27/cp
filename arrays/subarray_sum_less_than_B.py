class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start, end = 1, len(A)
        
        while start <= end:
            mid = start + (end - start) // 2
            
            j, subarray_sum = 0, 0
            while j < mid:
                subarray_sum += A[j]
                j += 1
            
            sum_is_greater = subarray_sum > B
            while j < len(A) and sum_is_greater != True:
                subarray_sum -= A[j - mid]
                subarray_sum += A[j]
                
                if subarray_sum > B:
                    sum_is_greater = True
                    break

                j += 1
                
            if sum_is_greater:
                end = mid - 1
            else:
                start = mid + 1
                
        return end