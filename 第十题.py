# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 例如，在下面的 3×4 的矩阵中包含单词 “ABCCED”（单词中的字母已标出）。
#深度优先遍历
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        l = len(word)
        visited = [[False] * m for _ in range(n)]

        def dfs(i, j, k):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or board[i][j] != word[k]:
                return False

            if k == l - 1:
                return True

            visited[i][j] = True
            res = dfs(i, j + 1, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i - 1, j, k + 1)
            visited[i][j] = False

            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False


def exist(board,word):
    n = len(board)
    m = len(board[0])
    l = len(word)
    visited = [[False]*m for _ in range(n)]
    def dfs(i,j,k):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or board[i][j] != word[k]:
            return False
        if k == l - 1:
            return True
        visited[i][j] = True
        res = dfs(i,j+1,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i-1,j,k+1)
        visited[i][j] = False

        return res
    for i in range(n):
        for j in range(m):
            if dfs(i,j,0):
                return True

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    q = Solution()
    print(q.exist(board,word))