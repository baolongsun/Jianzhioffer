# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]


def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
    res, k = [], 0
    while True:
        # 从左到右
        for j in range(l, r+1):
            res.append(matrix[t][j])
            k += 1
        if t+1 > b:
            break
        else:
            t += 1

        # 从上到下
        for i in range(t, b+1):
            res.append(matrix[i][r])
            k += 1
        if r-1 < l:
            break
        else:
            r -= 1

        # 从右到左
        for j in range(r, l-1, -1):
            res.append(matrix[b][j])
            k += 1
        if b-1 < t:
            break
        else:
            b -= 1

        # 从下到上
        for i in range(b, t-1, -1):
            res.append(matrix[i][l])
            k += 1
        if l+1 > r:
            break
        else:
            l += 1
    return res

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))
    print(spiralOrder2(matrix))

