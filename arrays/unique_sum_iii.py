class Solution:
    pathIncrements = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]
    

    def __init__(self):
        self.width = 0
        self.height = 0
    

    def recur(self, A, target, totalZeros, cur, traversedCells, vis):
        if target[0] == cur[0] and target[1] == cur[1]:
            # -1 because this param gets +1 for every traversable cell (except start)
            # even thoough the target is traversable it's not zero

            if traversedCells - 1 == totalZeros: return 1
            return 0

        vis[cur[0]][cur[1]] = 1
        res = 0

        for nextPath in Solution.pathIncrements:
            x, y = cur[0] + nextPath[0], cur[1] + nextPath[1]

            if x < self.width and x >= 0 and y < self.height and y >= 0 and A[x][y] != -1 and not vis[x][y]:
                vis[x][y] = 1
                res += self.recur(A, target, totalZeros, [x, y], traversedCells + 1, vis)
                vis[x][y] = 0

        return res


    def uniquePathsIII(self, A: List[List[int]]) -> int:
        self.width, self.height = len(A), len(A[0])
        totalZeros, start, target, vis = 0, [], [], []
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    totalZeros += 1
                elif A[i][j] == 1:
                    start = [i, j]
                elif A[i][j] == 2:
                    target = [i, j]

            vis.append([0]*len(A[i]))

        return self.recur(A, target, totalZeros, start, 0, vis)