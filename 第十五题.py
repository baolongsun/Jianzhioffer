# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

def myPow(x,n):
    res = 1
    y = n
    if n<0:
        y=-y
        x = 1/x
    while y>0:
        if y % 2 == 1:
            res = res * x
        x = x*x
        y = y//2
    return res
if __name__ == "__main__":
    print(myPow(2,10))