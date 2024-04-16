# 20 10
# 20 20
# 20 5
portfolio = 40
cost = [20, 20, 20]
price = [10, 20, 5]

m = 4
n = 40 + 1#容量加1

dp = [[0]*n for _ in range(m)]

for i in range(1,m):
    for j in range(1,n):
        if cost[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost[i-1]]+price[i-1])
print(dp[-1][-1])