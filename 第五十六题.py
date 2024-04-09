# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n)，空间复杂度是O(1)。

# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

def singleNumbers(nums):
    z = 0
    for i in range(len(nums)):
        z = z^nums[i]
    m = 1
    while(m&z)==0:
        m = m<<1
    x,y = 0,0
    for i in range(len(nums)):
        if (nums[i]&m)==0:
            # 结果为 0 的子数组，一边统计用异或统计 x
            x = x ^nums[i]
        else:
            # 结果为 1 的子数组，一边统计用异或统计 y
            y = y^nums[i]
    return [x,y]

# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31

def singleNumber(nums):
    res = [0]*32
    m = 1
    sum =0
    for i in range(32):
        for j in range(len(nums)):
            if (nums[j] & m) != 0:
                res[i] += 1
        res[i] %= 3
        sum += res[i]*m
        m <<= 1
    return sum

if __name__ == "__main__":
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(singleNumber(nums))
