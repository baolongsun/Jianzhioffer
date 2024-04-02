#割绳子 2
#长度m，切成n份 ,m>1,n>1，每个结果要取余
#(x1+x2)%p = (x1%p+x2%p)%p
#(x1*x2)%p = (x1%p*x2%p)%p,当x1,x2<p时,当x1,x2>p时不一定成立

#(a^n)%p = (a^n-1%p * a%p)%p
#        = (a^n-1%p * a)%p
#->   f(n) = (f(n-1)*q)%p
def cutting(m):
    if m <=2:
        return 1
    if m == 3:
        return 2
    res = m//3
    mod = m%3
    p = 1000000007
    if mod == 0:
        return pow(3,res)%p
    elif mod == 1:
        return (pow(3,res-1)*4)%p
    else:
        return (pow(3,res)*2)%p
def pow(a,n):
    res = 1
    p = 1000000007
    for i in range(1,n+1):
        res = (res*a)%p
    return res

if __name__ == "__main__":
    print(cutting(1000))

