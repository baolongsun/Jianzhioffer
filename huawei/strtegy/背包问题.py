#0,1背包问题
N = 4  # 物品数量
W = 10  # 背包容量
v = [0, 1, 3, 5, 9]  # 物品价值
w = [0, 2, 3, 4, 7]  # 物品重量

# dp[i][j] 物品 容量
dp = [[0]*(W+1) for _ in range(N+1)] # # dp[i][j] 表示前 i 个物品放入容量为 j 的背包的最大价值

for i in range(1,N+1):#物品排序
    for j in range(1,W+1):#容量
        if w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
ans = dp[N][W]
print(ans)

#完全背包问题,每个物品可以被多次取用
for i in range(1,N+1):#物品排序
    for j in range(1,W+1):#容量
        if w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])

ans = dp[N][W]
print(ans)

