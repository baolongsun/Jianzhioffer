# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

def nthUglyNumber(n):
    dp = [0] * (n+1)
    dp[1] = 1
    a,b,c = 1,1,1

    for i in range(2,n+1):
        dp[i] = min(dp[a]*2,dp[b]*3,dp[c]*5)
        if dp[i] == dp[a]*2:
            a += 1
        if dp[i] == dp[b]*3:
            b += 1
        if dp[i] == dp[c]*5:
            c += 1

    return dp

if __name__ == "__main__":
    bak = nthUglyNumber(100)
    for iter in range(100):
       print(f"index:{iter},num:{bak[iter]}")
