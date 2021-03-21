class Solution:
	def maxArea(self, A):
        '''
        start, end
        0, N - 1
        
        max_area = (end - start) * min(A[start], A[end])        
        
        n1, n2
        '''
        
        start, end = 0, len(A) - 1
        max_area = 0
        
        while start < end:
            min_height = min(A[end], A[start])
            max_area = max(max_area, (end - start) * min_height)
            
            if min_height == A[start]:
                start += 1
            else:
                end -= 1
                
        return max_area