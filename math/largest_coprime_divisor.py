def gcdFunc(a, b):
    if b == 0:
        return a
    else:
        return gcdFunc(b, a % b)

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def cpFact(self, A, B):
        
        gcd = gcdFunc(A, B)
        while gcd != 1:
            A //= gcd
            gcd = gcdFunc(A, B)
            
        return A