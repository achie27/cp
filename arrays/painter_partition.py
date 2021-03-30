class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, a, b, c):

        low, high = max(c) - 1, sum(c)
        while high - low > 1:
            mid = low + (high - low)//2
            
            painters = self.paintersRequired(c, mid)
            if painters > a:
                low = mid
            else:
                high = mid

        return (high * b) % 10000003
    
    
    def paintersRequired(self, c, paintLimit):
        i, painters = 0, 1
        curPainted, maxWork = 0, 0
        
        while i < len(c):
            curPainted += c[i]
            
            if curPainted > paintLimit:
                painters += 1
                curPainted = c[i]
                
            i += 1

        return painters