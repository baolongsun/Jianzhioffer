# 若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
# 输入: [0,0,1,2,5]
# 输出: True

# 限制
# 数组长度为 5
# 数组的数取值为 [0, 13] .

def isStraight(nums):
    #要构成一个顺子,需要满足两个条件
    #1.不存在重复的数,大小王除外
    #2.最大值-最小值<5,大小王除外

    s = set()
    max_num,min_num = -1,20
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        if nums[i] in s:
            return False
        s.add(nums[i])
        max_num = max(nums[i],max_num)
        min_num = min(nums[i],min_num)
    return max_num-min_num<5

if __name__ == "__main__":
    nums = [1,2,0,0,6]
    print(isStraight(nums))

