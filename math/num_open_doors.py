import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        '''
        -> All doors with numbers having odd factors will remain open
        -> Perfect squares have odd number of factors
        -> Number of perfect squares can be calculated by 
                floor(sqrt(q)) + ceil(sqrt(p)) - 1
        '''
        return int(math.floor(math.sqrt(A)))