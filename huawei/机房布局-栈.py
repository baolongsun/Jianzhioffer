def result1():
    n = len(s)
    stack = []
    stick = False # 是否形成了共享电箱
    for i in range(n):
        if s[i] == "M":
            # 如果机柜A两边都是机柜，或者没有间隔，则无法给机柜A放电箱，返回-1
            left = (i-1) < 0 or s[i-1] == "M" # 判断左边是否有M，或者为边界
            right = (i+1>=n) or s[i+1] == "M" # 判断右边是否有M，或者为边界
            if left and right:
                return -1
            # 求出最少电箱问题，转化为区间交集问题
            ran = [max(0, i-1), min(n-1,i+1)]
            if len(stack)>0 and not stick:# stack非空，并且并没有形成共享电箱，才能弹出。
                e1 = stack[-1][1] # 栈顶元素区间结束
                s2 = ran[0] # 区间开始的
                if e1 == s2:
                    stack.pop()
                    stick = True
            else:
                stick = False
            stack.append(ran)
    return len(stack)

def result2():
    n = len(s)
    ans = 0
    i = 0
    while i < n:
        if s[i] == "M":
            # 如果当前为机柜
            # 优先将电箱放到机柜的右边，如果机柜右边有间隔I的话，还要别越界
            if i+1<n and s[i+1] == "I":
                ans += 1
                # 如果放成功了的话，第i个位置为机柜，i+1的位置为电箱
                # 那么第i+2无论是机柜，还是空位，还是电箱都可以。所以这里i+2
                i += 2 # 注意要理解这个。
            # 上面右边搞不定，我们只能搞左边了。
            elif i-1>0 and s[i-1] == "I":
                # 如果左边没越界，并且左边有空位
                ans += 1
            # 两边都搞不定，只能返回无法放入电箱了
            else:
                ans = -1
                break
        i += 1 #往后走一个了。
    return ans
s = 'MIMIM'
print(result1())
