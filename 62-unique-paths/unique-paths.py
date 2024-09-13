class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ##########DP SOLUTION##########
        dp = [[1] * n for i in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row- 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]



        ##########RECURSIVE SOLUTION##########
        # if m == 1 or n == 1:
        #     return 1

        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


        ##########DFS SOLUTION##########
        # def dfs(i, j, visited, paths):

        #     if i == m - 1 and j == n - 1:
        #         paths[0] += 1
        #         return paths[0]

        #     for idir, jdir in directions:
        #         newi = i + idir
        #         newj = j + jdir
        #         if (0 <= newi < m) and (0 <= newj < n) and (newi, newj) not in visited:
        #             visited.add((newi, newj))
        #             dfs(newi, newj, visited, paths)
        #             visited.remove((newi, newj))
        #     return paths[0]

        # directions = [[1,0],[0,1]]
        # visited = set()
        # visited.add((0,0))
        # paths = [0]

        # paths = dfs(0, 0, visited, paths)
        # return paths



        


        