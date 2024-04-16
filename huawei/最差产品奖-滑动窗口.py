from collections import deque
def maxSlidingWindow(nums,k):
    if not nums or len(nums) < k:
        return []
    queue = deque()#放可能成为最大值的下标的,最大值在最左边,queue.popleft()是队列顺序出
    res = []

    for i in range(len(nums)):
        while queue and nums[queue[-1]] <= nums[i]:
            queue.pop()
        queue.append(i)

        if queue[0] == i-k:
            queue.popleft()
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res

def maxAltitude(heights,limit):
    if not heights or limit == 0:return []
    queue = deque()
    #未形成窗口
    for i in range(limit):
        while queue and queue[-1] < heights[i]:
            queue.pop()
        queue.append(heights[i])
    res = [queue[0]]
    #形成窗口后
    for i in range(limit,len(heights)):
        if queue[0] == heights[i-limit]:#判断最大的那个值新加一步是否跳出
            queue.popleft()
        while queue and queue[-1] < heights[i]:
            queue.pop()
        queue.append(heights[i])
        res.append(queue[0])
    return res

def minSlidingWindow(nums,interval):
    if not nums:
        return []
    queue = deque()
    res = []
    for k in range(len(nums)):
        while queue and nums[queue[-1]] >= nums[k]:
            queue.pop()
        queue.append(k)
        if queue[0] == k - interval:
            queue.popleft()
        if k >= interval - 1:
            res.append(nums[queue[0]])
    return res


if __name__ == "__main__":
    array = [12,3,8,6,5]
    print(maxSlidingWindow(array,3))
    print(minSlidingWindow(array,3))