class Solution:
    def partition(self, A: str) -> List[List[str]]:
        n = len(A)
        allPar = []

        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while j > i:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                
            return True
            
        def recur(curIndex, partitions):
            if curIndex == n:
                allPar.append(partitions[:])
                return
            
            for i in range(curIndex, n):
                curStr = A[curIndex : i + 1]
                if isPalindrome(curStr):
                    partitions.append(curStr)
                    recur(i + 1, partitions)
                    partitions.pop()

        recur(0, [])
        return allPar
