# PS：本问题描述有点多，其实就是字面意思了，就是要注意节点相交 和 节点值相等不是一回事。
#
# 输入两个链表，找出它们的第一个公共节点。
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def getIntersectionNode(headA,headB):
    if not headA or not headB:
        return None
    A,B = headA,headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA

    return A

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.next = n2
    n2.next = n4
    n3.next = n6
    n4.next = n5
    intersection = getIntersectionNode(n1,n3)
    print(intersection.val) if intersection else print('')