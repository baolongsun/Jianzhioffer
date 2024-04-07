# 最小的k个数
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

def getLeastNumbers(arr,k):
    if not arr or len(arr) == 0 or k==0:
        return []
    return quickFind(arr,0,len(arr)-1,k)

def quickFind(arr,left,right,k):
    i = partition(arr,left,right)
    if i+1 == k:
        return arr[:k]
    elif i + 1 > k:
        return quickFind(arr,left,i-1,k)
    else:
        return quickFind(arr,i+1,right,k)

def partition(arr,left,right):
    pivot = arr[left]

    i = left+1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i >= j:
            break

        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    arr[left] = arr[j]
    arr[j] = pivot
    return j

if __name__ == "__main__":
    print(getLeastNumbers([8,3,7,2,10,6,9],3))