#斐波那契数列

#这种写法会占用大量的空间
def Fib(n):
    if n<=1:
        return n
    return Fib(n-1)+Fib(n-2)

# O(n),O(n)
#自上而下,将重复计算的结果保存到数组中
def f(n,tag_list):
    if n<=1:
        return n
    if(tag_list[n]!=-1):
        return tag_list[n]
    else:
        sum = f(n-1,tag_list)+f(n-2,tag_list)
        tag_list[n] = sum
        return sum
def Fib2(n):
    tag_list = []
    for i in range(n+1):#此处是一个问题n+1
        tag_list.append(-1)
    return f(n,tag_list)
#自底向上
#O(n) O(1)
def Fib3(n):
    if n<=1:
        return n
    a,b = 0,1
    for i in range(2,n+1):
        c = (a+b) % 1000000007
        a = b
        b = c
    return c

if __name__ == "__main__":
    for i in range(10):
        print(f"{i}:{Fib(i)},{Fib2(i)},{Fib3(i)}")