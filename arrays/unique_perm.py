class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
	    n = len(A)
	    allPerms = []

        def recur(perm, cur):
            if cur == n:
                allPerms.append(perm[:])
                return
            
            seen = {}
            for i in range(cur, n):
                if perm[i] not in seen:
                    perm[cur], perm[i] = perm[i], perm[cur]
                    recur(perm, cur + 1)
                    perm[cur], perm[i] = perm[i], perm[cur]

                seen[perm[i]] = 1

        recur(A, 0)
        return allPerms