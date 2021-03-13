class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        num, power = 0, 1
        
        while A > 0:
            num += A%2 * (5**power)
            A//=2
            power+=1
            
        return num