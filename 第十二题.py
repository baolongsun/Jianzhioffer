#割绳子 1
#长度m，切成n份 ,m>1,n>1
#(x/2)^2 > x 当x大于等于5时成立,因此长度大于5时需要进行割绳子
#绳子切成2,3,4的类型,2不能再继续切了，尽可能切出3，2与4不能同时出现
#2*4要改成3*3

class Solution:
    def cuttingRope(self, bamboo_len: int) -> int:
        if bamboo_len <= 3:
            return bamboo_len - 1

        quotient, remainder = bamboo_len // 3, bamboo_len % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * (3+1)
        else:
            return 3 ** quotient * 2

if __name__ == "__main__":
    q = Solution()
    print(q.cuttingRope(1000))
