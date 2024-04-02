# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为 汉明重量).）。

def hammingWight(n):
    sum = 0
    while n != 0:
        n = n & (n-1)#n&(n-1)可以消除n最右边的1个1,二进制表示
        sum+=1
    return sum

if __name__ == "__main__":
    print(hammingWight(11))