# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
#
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getKthFromEnd(head,k):
    if head == None:
        return
    fast = head
    slow = head
    for _ in range(k):
        if fast.next == None:
            return
        fast = fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow

if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h1.next = h2
    h2.next = h3
    h3.next = h4

    print(getKthFromEnd(h1,2).val)



