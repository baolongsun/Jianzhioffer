k = 3
array = [1,2,3,1,2,3,3,4,42,2,32,3,2,3,4,5,6,2,1,3,4,5,2,3,4]
start = end = 0
num_dict = {}
res = []
total_num = 0
while(start<len(array) and end < len(array)):
    if array[end] not in num_dict:
        num_dict[array[end]] = 1
    if num_dict[array[end]] >= k:
        res.append(array[start:end+1])
        num_dict[array[start]] -= 1
        start += 1
        total_num += len(array) - end
    else:
        if end + 1 < len(array):
            end += 1
            if array[end] not in num_dict:
                num_dict[array[end]] = 1
            else:
                num_dict[array[end]] += 1
        else:
            num_dict[array[start]] -= 1
            start += 1

def result(n,k,arr):
    ans = 0
    for i in range(n):
        count = {}
        for j in range(i, n):
            c = arr[j]
            if count.get(c) is None:
                count[c] = 1
            else:
                count[c] += 1
            if count[c]>=k:
                ans += n-j
                break
    return ans
print(res)
print(total_num)
print("*"*10)
print(result(len(array),k,array))




