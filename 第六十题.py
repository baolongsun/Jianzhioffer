# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
#
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

def dicesProbability(n):
    dp = [[0]*(6*n+1) for _ in range(n+1)]
    for i in range(1,7):
        dp[1][i] = 1

    for i in range(2,n+1):
        for j in range(i,6*i+1):
            for k in range(1,7):
                if j < k:
                    break
                dp[i][j] += dp[i-1][j-k]

    res = [0]*(5*n+1)
    index = 0
    s = pow(6,n)
    for i in range(n,6*n+1):
        res[index] = float(dp[n][i])/s
        index += 1

    return res

if __name__ == "__main__":
    print(dicesProbability(2))