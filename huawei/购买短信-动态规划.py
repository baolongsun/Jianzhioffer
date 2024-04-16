#容量 6
# 10 20 30 40 60
#输出 70
# 本金
max_pr = 6
price = [10,20,30,40,60]
cost = list(range(1,len(price)+1))

N = max_pr + 1#列
M = len(price) + 1#行
dp = [[0]*N for _ in range(M)]
for i in range(1,M):
    for j in range(1,N):
        if cost[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost[i-1]] + price[i-1])

print(dp[-1][-1])




