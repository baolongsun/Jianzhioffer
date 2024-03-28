# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or k < self.sum(i) + self.sum(j):
                return 0

            visited[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)

    def sum(self, x):
        res = 0
        while x != 0:
            res += x % 10
            x //= 10
        return res

def movingCount(m,n,k):
    visited = [[False]*n for _ in range(m)]
    def sum(x):
        res = 0
        while x != 0:
            res += x % 10
            x //=10
        return res
    def dfs(i,j):
        if i<0 or j<0 or i>= m or j>=n or visited[i][j] or k < sum(i) + sum(j):
            return 0
        visited[i][j]=True
        return 1+dfs(i+1,j) + dfs(i,j+1)
    return dfs(0,0)


if __name__ == "__main__":
    q = Solution()
    print(q.movingCount(30,30,10),end='\n')
    print(movingCount(30,30,10))