#二分
#maxcapacity,将每个桶的超出容量截断
#左边界为平均每个桶的球数
#有边界为球数最多的桶的球数
#将mid值设为maxcapacity
#若剩余球数>sum maxcap过大 需要减小,更新右边界为mid
#若剩余球数<sum,maxcap过小,需要增加,更新左边界为mid,并更新数组为当前的临时数组
import copy

def subList(array_list,num):
    temp = copy.deepcopy(array_list)
    for i in range(len(temp)):
        temp[i] = num if temp[i]>num else temp[i]
    return temp

max_liquid = 24
bucket = [2,3,2,5,5,1,4]
bucet_len = len(bucket)
return_result = [0 for _ in bucket]
high = max(bucket)
low = min(bucket)
while (low <= high):
    mid = (high + low) // 2
    temp_bucket = subList(bucket,mid)
    temp_sum = sum(temp_bucket)
    if temp_sum < max_liquid:
        return_result = temp_bucket
        low = mid+1
    elif temp_sum > max_liquid:
        high = mid-1
    else:
        return_result = temp_bucket
        break
print(return_result)




