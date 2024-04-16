pos_list = [1,0,1,2,1,0,1,1,0,1]#两边
maxFriend = 0
leftFriend = 0
rightFriend = 0
#遍历工位
for i in range(len(pos_list)):
    if pos_list[i] == 1:#老员工
        leftFriend += 1
    elif pos_list[i] == 2:#障碍
        leftFriend = 0
    elif pos_list[i] == 0:#空位
        for j in range(i+1,len(pos_list)):
            if pos_list[j] == 1:
                rightFriend += 1
            elif pos_list[j] == 0 or pos_list[j] == 2:
                break
        temp_max = leftFriend+ rightFriend
        maxFriend = max(temp_max,maxFriend)
        leftFriend = 0
        rightFriend = 0
print(maxFriend)

