#若两个列表存在2个及以上数据一样,则可以进行合并

def mergeTwolist(a,b):
    return list(set(list(a) + list(b)))

def mergeBool(a,b):
    count = 0
    for item in b:
        if item in a:
            count += 1
    return count >= 2

def decideBool(input_list):
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            temp1 = input_list[i]
            temp2 = input_list[j]
            if mergeBool(temp1,temp2):
                input_list[i] = mergeTwolist(temp1,temp2)
                input_list.pop(j)
                return True


if __name__ == "__main__":
    # input_list = [[10],[4,2,1],[9],[3,6,9,2],[6,3,4],[8]]
    input_list = [[11]]
    input_len = len(input_list)

    while decideBool(input_list):
        print("change")
    print(input_list)
    # tag = False
    # for i in range(1,len(input_list)):
    #     tag = mergeBool(input_list[0],input_list[i])
    #     if tag:
    #         temp = mergeTwolist(input_list[0],input_list[i])
    #         input_list.pop(i)
    #         input_list.pop(0)
    #         input_list.append(temp)
    #         break
    # print(input_list)

