#青蛙跳台阶
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 输入：n = 0
# 输出：1
# 输入：n = 7
# 输出：21
#得到递推公式
# f(n) = f(n-1) + f(n-2)
def numWays(n):
    if n <= 1:
        return 1
    a = 1
    b = 1
    c = 0
    for i in range(2,n+1):
        c = (a+b)%1000000007
        a = b
        b = c
    return c

if __name__ == "__main__":
    for n in range(10):
        print(f"{n}:{numWays(n)}")