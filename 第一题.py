# 找出数组中重复的数字。
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 `0～n-1`的范围内。数组中某些数字是重复的，但不知
# 道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

#排序后,遍历一遍找到前后不一致的数     时间O(nlogn) 空间O(1)
#构建hash表,映射                  时间O(n)     空间O(n)
#关键点,在遇到数值范围0->n-1时,可以考虑构建指标集的方法

def findRepeatNumber(num:list)->int:
    for i in range(len(num)):
        if num[i] != i:#表示当前位置的数不能对应到正确位置,下面要增加对应到正确位置的逻辑
            temp = num[num[i]]
            if num[i] == temp:#交换位置时发现重复
                return num[i]
            else:
                num[num[i]] = num[i]#交换位置
                num[i] = temp
    return -1

if __name__ == "__main__":
    a = [1,3,4,5,6,2]
    print(findRepeatNumber(a))
