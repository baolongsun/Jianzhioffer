# 第1个字符串:R
# 第2个字符串:BR
# 第3个字符串:RBBR
# 第4个字符串:BRRBRBBR
# 第5个字符串:RBBRBRRBBRRBRBBR

def pq(n,k):#Return True或者False
    if n <= 1:
        return True
    total_num = 2**(n-2)
    if k <= total_num:
        return not pq(n-1,k)
    else:
        return pq(n-1,k-total_num)
if __name__ == "__main__":
    print(pq(4,1))