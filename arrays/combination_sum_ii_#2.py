class Solution:
    def __init__(self):
        self.allCombs = []

    def recur(self, candidates, target, cur, curComb, curCombSum):
        if target < curCombSum:
            return
        
        if target == curCombSum:
            self.allCombs.append(curComb[:])
            return
        
        for i in range(cur, len(candidates)):
            if i > cur and candidates[i] == candidates[i - 1]:
                continue
            
            curComb.append(candidates[i])
            self.recur(candidates, target, i + 1, curComb, curCombSum + candidates[i])
            curComb.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        self.recur(candidates, target, 0, [], 0)
        return self.allCombs
