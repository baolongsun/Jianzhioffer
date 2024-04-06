# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。

# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

#模型定义
# dp[i] 表示以坐标i结尾的连续数组的最大值
# dp[i] = max(dp[i-1]+nums[i],nums[i])
# 初始条件 dp[0] = nums[0]


def maxSubArray(nums):
    dp = [0 for _ in nums]
    dp[0] = nums[0]
    total_max = dp[0]
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
        total_max = max(total_max,dp[i])
    return total_max

if __name__ == "__main__":
    print(maxSubArray([-2,1,3,-5,6,7,-4]))