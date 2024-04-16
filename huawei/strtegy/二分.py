input_list = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(input_list) - 1
num = 10
while left <= right:
    mid = (left + right)//2
    if input_list[mid] > num:
        right = mid - 1
    elif input_list[mid] < num:
        left = mid + 1
    else:
        print(mid)
        break