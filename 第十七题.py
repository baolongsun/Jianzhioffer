# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head,val):
    if head == None:
        return
    if head.val == val:
        return head.next
    fast = head.next
    slow = head
    while(fast):
        if fast.val == val:
            slow.next = fast.next
            return head
        slow = slow.next
        fast = fast.next
    return head

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    #1,2,3,4
    n1 = deleteNode(n1,1)
    temp = n1
    while(temp):
        print(temp.val)
        temp = temp.next


