# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1,l2):
    merge = ListNode(0)
    temp = merge
    if l1==None and l2 ==None:
        return None
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if not l1:
        temp.next = l2
    else:
        temp.next = l1
    return  merge.next


if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h1.next = h2
    h2.next = h3
    h3.next = h4

    h5 = ListNode(1)
    h6 = ListNode(2)
    h7 = ListNode(3)
    h8 = ListNode(4)
    h5.next = h6
    h6.next = h7
    h7.next = h8

    mergeLink = mergeTwoLists(h1,h5)
    temp = mergeLink
    while temp:
        print(temp.val)
        temp = temp.next
