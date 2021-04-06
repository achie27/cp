class Solution:
    def getPermutation(self, n: int, k: int) -> str:        
        # make the sequence indexing 0-based
        # this will help during %-ing by giving the actual next elem
        # in the required perm
        k -= 1

        def fact(x):
            if x <= 1: return 1
            return x * fact(x - 1)

        def recur(curPerm, rank):
            # print(curPerm, rank)

            if len(curPerm) == 1:
                return curPerm[0]

            f = fact(len(curPerm) - 1)
            nextElem = curPerm[rank//f]

            curPerm.remove(nextElem)
            return nextElem + recur(curPerm, rank % f)

        return recur([str(x) for x in range(1, n + 1)], k)