class Solution:
	# @return an integer
	def solve(self, A, B, C):
        '''
        
        A : [ 1, 4, 5, 8, 10 ]
        B : [ 6, 9, 15 ]
        C : [ 2, 3, 6, 6 ]
        
        A : [ 1, 8 ]
        B : [ 4, 6, 9, 10, 15 ]
        C : [ 2, 3, 6, 10 ]
        
        '''
        
        a, b, c = 0, 0, 0
        lenA, lenB, lenC = len(A), len(B), len(C)
        
        minVal = float('inf')
        while a < lenA and b < lenB and c < lenC:
            minEle = min(A[a], B[b], C[c])
            maxEle = max(A[a], B[b], C[c])
            minVal = min(minVal, maxEle - minEle)
            
            if A[a] == minEle:
                a += 1
            elif B[b] == minEle:
                b += 1
            else:
                c += 1
                
        return minVal
            
            