def findPath(array):
    if not array:
        return 0
    m = len(array)
    n = len(array[0])
    visited = [[0]*n for _ in range(m)]
    def dfs(i,j):
        global count
        visited[i][j] = 1
        for nx,ny in [[-1,0],[1,0],[0,-1],[0,1]]:
            tx = i + nx
            ty = j + ny
            if 0<=tx<m and 0<=ty<n and abs(array[tx][ty] - array[i][j]) <= 1 and not visited[tx][ty]:
                count += 1
                dfs(tx,ty)
    def bfs(i,j):
        global count
        queue = [[i,j]]
        while queue:
            i,j = queue.pop(0)
            visited[i][j] = 1
            for nx,ny in [[-1,0],[1,0],[0,1],[0,-1]]:
                tx = i + nx
                ty = j + ny
                if 0<=tx<m and 0<=ty<n and abs(array[tx][ty]-array[i][j]) <= 1 and not visited[tx][ty]:
                    count += 1
                    queue.append([tx,ty])
    for i in range(m):
        for j in range(n):
            dfs(i,j)
    return count

if __name__ == "__main__":
    array = [[1,2,5,2],[2,4,4,5],[3,5,7,1],[4,6,2,4]]
    array2 = [[1,2,3],[4,5,6],[10,11,12]]
    count = 0
    print(findPath(array2))
