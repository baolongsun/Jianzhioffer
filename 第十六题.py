# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#若数字溢出,考虑全排列

# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]

def printNumbers(n):
     sum = 10 ** n
     result = [i for i in range(sum)]
     return result

if __name__ == "__main__":
    print(printNumbers(2))