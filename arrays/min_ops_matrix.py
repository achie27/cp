class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        flattened_a, mod, res = [], A[0][0]%B, 0
        for e in A:
            for f in e:
                if mod != f%B:
                    res = -1
                    break
                flattened_a.append(f)
            if res == -1:
                break
        
        if res == -1:
            return -1
        
        flattened_a.sort()
        
        equate_to = flattened_a[len(flattened_a)//2]
        steps = 0
        
        for e in flattened_a:
            diff = 0
            if e <= equate_to:
                diff = equate_to - e
            else:
                diff = e - equate_to

            steps += diff//B
            
        return steps