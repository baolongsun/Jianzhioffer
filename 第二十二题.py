#反转链表 递归 原地

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归方式
def reverseLink(head):
    if head == None or head.next == None:
        return head
    temp = reverseLink(head.next)
    head.next.next = head
    head.next = None
    return temp

def reverseLink2(head):
    if head == None or head.next == None:
        return head
    cur = head
    pre = None
    while(cur):
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h1.next = h2
    h2.next = h3
    h3.next = h4

    temp = reverseLink2(h1)
    while temp:
        print(temp.val)
        temp = temp.next