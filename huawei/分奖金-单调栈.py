#单调栈:栈中元素为单调排列
def result(arr,n):
    stack = []#存放位置以及对应的值
    nexbig = [-1]*n#初始化位置为-1,否则存放第一个比其大的数字
    for i in range(n):
        while stack:
            idx,val = stack[-1]#栈顶元素
            if arr[i] > val:
                stack.pop()
                nexbig[idx] = i
            else:
                break
        stack.append([i,arr[i]])
    ans = []
    for i in range(n):
        idx = nexbig[i]
        if idx == -1:
            ans.append(arr[i])
        else:
            ans.append((idx-i)*(arr[idx]-arr[i]))
    return ans

if __name__ == "__main__":
    arr = [2,10,3]
    n = 3
    print(result(arr,n))