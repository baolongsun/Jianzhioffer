# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

#dp[i]表示index为i的排列方式有多少
#dp[i] = dp[i-1]+dp[i-2] 若 num[i-1:i]>10且小于25
#dp[i] = dp[i-1]         若 num[i-1:i]>25或者<10
#dp[0] = 1;dp[1] = 1

def translateNum(num:int):
    if num <= 9:
        return 1
    base = list(str(num))
    base_len = len(base)
    dp = [1 for _ in base]
    temp = int(base[1]) + int(base[0]) * 10
    if temp >9 and temp <=25:
        dp[1] = 2
    else:
        dp[1] = 1
    for i in range(2,base_len):
        temp = int(base[i])+int(base[i-1])*10
        if temp > 9 and temp <= 25:
            dp[i] = dp[i-1]+dp[i-2]
        else:
            dp[i] = dp[i-1]
    return dp

if __name__ == "__main__":
    print(translateNum(12258))