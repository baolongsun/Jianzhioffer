#调整数组顺序，奇数位于偶数前面
#类似于快排的思想，双指针
def exchange(array_list):
    if array_list == None or len(array_list) == 0:
        return
    start = 0
    end = len(array_list) - 1
    while(start<end):
        while(start<end and array_list[start]%2 != 0):
            start +=1
        while(start<end and array_list[end]%2 != 1):
            end -= 1
        temp = array_list[start]
        array_list[start] = array_list[end]
        array_list[end] = temp
    return array_list

if __name__ == "__main__":
    test_case = [1,2,3,4,5]
    print(exchange(test_case))
