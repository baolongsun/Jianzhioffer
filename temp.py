class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

def reverseLink(head:Node)->Node:
    if head.next == None:#跳出递归的边界条件
        return head
    new_node = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return new_node


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    #打印链表
    temp = node1
    while temp:
        print(temp.value)
        temp = temp.next
    print("-"*10)
    #反转链表
    new = reverseLink(node1)
    temp = new
    while temp:
        print(temp.value)
        temp = temp.next