# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
# 输入：head = [1,3,2]
# 输出：[2,3,1]
# 从右边往左填充

#反转链表         时间  空间
#用栈的方法  O(n) O(n)
#反转链表 1.递归  O(n) O(n)
#       2.原地  O(n) O(n)
#              O(n) O(1)
from link import Node, SingleLinkList

def reverseLink(head:Node):
    if not head:
        return []
    count = 0
    temp = head
    #统计链表节点个数
    while temp:
        count += 1
        temp = temp.next
    res = [0]*count
    k = count - 1#从右往左填充数组
    while head:
        res[k]=head.value;k-=1
        head = head.next
    return res

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    Link = SingleLinkList()
    Link._head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(reverseLink(Link._head))



