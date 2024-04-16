#左边元素乘为1,右边连续乘为1
num = [1,2,3,4,5,120]
num.insert(0,1)
num.append(1)
product = 1
for i in num:
    product = product * i
left_init = 1
for i in range(1,len(num)):
    left_init = left_init*num[i-1]
    product = product//num[i]
    if left_init == product:
        print(i)


#加法形式
class Solution:
    def pivotIndex(self, nums) -> int:
        new_num = [0 for i in range(len(nums)+2)]
        right_sum = 0
        for i in range(len(nums)):
            new_num[i+1] = nums[i]
            right_sum += nums[i]
        left_sum = 0
        for i in range(1,len(new_num)-1):
            left_sum = left_sum + new_num[i-1]
            right_sum = right_sum - new_num[i]
            if left_sum == right_sum:
                return i-1
        return -1