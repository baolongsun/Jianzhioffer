# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

#摩尔投票

def majorityElement(nums):
    if len(nums) <= 2:
        return nums[0]

    x = nums[0]
    sum = 1

    for i in range(1, len(nums)):
        if sum == 0:
            x = nums[i]
            sum = 1
        else:
            if x == nums[i]:
                sum += 1
            else:
                sum -= 1
    return x

if __name__ == "__main__":
    print(majorityElement([1,2,3,1,1,1,1]))
