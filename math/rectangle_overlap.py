class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
        '''
            8 e,h              g,h
            7
            6
            5     a,d          c,d
            4 e,f              g,f 
            3
            2     a,b          c,b  
            1
            0 1 2 3 4 5 6 7 8 9 10
        '''
        
        return 0 if A >= G or E >= C or D <= F or H <= B else 1
    