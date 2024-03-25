# 请实现一个函数，把字符串 s 中的每个空格替换成”%20″。
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

#思路
#扩充数组,然后从后往前遍历,遇到空格则%20,否则直接写入

def replaceSpace(inputString:str)->str:
    count = 0
    for i in inputString:
        if i == " ":
            count+=1
    #需要记录的数据长度
    data_bk = [' ']*(count*2+len(inputString))#可以使用''.join进行拼出字符串
    k = len(data_bk)-1
    for i in range(len(inputString)-1,-1,-1):#注意第二个值为-1
        if inputString[i] != " ":
            data_bk[k] = inputString[i]
            k-=1
        else:
            data_bk[k] = '0';k-=1
            data_bk[k] = '2';k-=1
            data_bk[k] = '%';k-=1
    return "".join(data_bk)

if __name__ == "__main__":
    a = 'qwerr sdfd wss'
    print(replaceSpace(a))