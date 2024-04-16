# dp[i][j]#表示str1的前i个和str2的前j个(以i和j结尾)的相同子串的数目

def subStr(str1,str2):
    m = len(str1)
    n = len(str2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_num = 0
    index = [0,0]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            if dp[i][j] > max_num:
                index = [i-1,j-1]
                max_num = dp[i][j]
    end = index[1]
    while dp[index[0]][index[1]] != 0:
        index[0]-=1;index[1]-=1
    start = index[1]
    return max_num,str2[start:end+1]


if __name__ == "__main__":
    num,substr = subStr('qqqqqxabcdfd','qxabcdfdddd')
    print(num,substr)
