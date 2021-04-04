class Solution:
    def __init__(self):
        self.allCombs = []
        
    def recur(self, A, B, cur, comb, combSum):

        if B < combSum:
            return
        
        if B == combSum and comb not in self.allCombs:
            self.allCombs.append(comb[:])
            return

        for i in range(cur, len(A)):
            # newComb = comb[:]
            # newComb.append(A[i])
            # self.recur(A, B, i + 1, newComb, combSum + A[i])

            comb.append(A[i])
            self.recur(A, B, i + 1, comb, combSum + A[i])
            comb.pop()

    def combinationSum(self, A, B):
        A.sort()
        self.recur(A, B, 0, [], 0)
        
        return self.allCombs