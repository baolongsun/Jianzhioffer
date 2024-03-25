# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。

#可以使用二分查找 n*logn


def findNumberIn2DArray(matrix:list,target:int)->bool:
    if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
        return False
    row = len(matrix)
    column = len(matrix[0])
    #从左下角元素开始便利,其上方一列的数据小于它,右方一行数据都大于它
    init_row = row-1;init_column = 0
    while(init_row>=0 and init_column <= column-1):
        if matrix[init_row][init_column]>target:
            init_row-=1
        elif matrix[init_row][init_column]<target:
            init_column+=1
        else:
            return True
    return False



if __name__ == "__main__":
    a = [[1,2,3],[3,4,6]]
    print(findNumberIn2DArray(a,2))