# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]

#有序数组,此时可以使用二分法,结合题意更适合双指针
def twoSum(nums,target):
    if not nums or len(nums) < 2:
        return []
    start = 0
    end = len(nums) - 1
    while(start<end):
        temp = nums[start] + nums[end]
        if temp == target:
            return [nums[start],nums[end]]
        elif temp < target:
            start += 1
        else:
            end -= 1
    return []


# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]

#使用滑动窗口解决
def findContinuousSequence(target):
    res = []
    i,j = 1,1
    sum_ = 1
    while i <= target//2:
        if sum_ < target:
            j += 1
            sum_ += j
        elif sum_ > target:
            sum_ -= i
            i += 1
        else:
            temp = list(range(i,j+1))
            sum_ -= i
            i += 1
            j += 1
            sum_ += j
            res.append(temp)
    return res


if __name__ == "__main__":
    temp = [1,2,3,4,5,6,7]
    print(twoSum(temp,3))
    print(findContinuousSequence(9))
