# 复杂链表的复制
class Node:
    def __init__(self,x,next=None,random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomListBase(head):
    if not head:
        return None
    #复制链表节点
    cur = head
    while cur:
        next = cur.next
        cur.next = Node(cur.val)
        cur.next.next = next
        cur = next

    #复制随机节点
    cur = head
    while cur:
        curNew = cur.next
        curNew.random = cur.random.next if cur.random else None
        cur = cur.next.next

    #拆分,将A->A1->B->B1->C->C1拆分为A->B->C和A1->B1->C1
    headNew = head.next
    cur = head
    curNew = head.next
    while cur:
        cur.next = cur.next.next
        cur = cur.next
        curNew.next = cur.next if cur else None
        curNew = curNew.net

    return headNew
def copyRandomList(head):
    if not head:
        return None
    key_map = dict()
    cur = head
    while cur:
        key_map[cur] = Node(cur.val)#原始:新节点
        cur = cur.next
    cur = head
    while cur:
        if cur.next:
            key_map[cur].next = key_map[cur.next]
        if cur.random:
            key_map[cur].random = key_map[cur.random]
        cur = cur.next
    return key_map[head]







