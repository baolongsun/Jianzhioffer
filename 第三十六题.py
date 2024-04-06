# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。
#二叉搜索树,中序遍历后为升序排列
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root):
    """
    :type root: Node
    :rtype: Node
    """
    if not root:
        return None

    queue = []
    inOrder(root, queue)
    head = queue.pop(0)
    pre = head

    while queue:
        cur = queue.pop(0)
        pre.right = cur
        cur.left = pre
        pre = cur

    pre.right = head
    head.left = pre

    return head

def inOrder(root, queue):
    if not root:
        return
    inOrder(root.left, queue)
    queue.append(root)
    inOrder(root.right, queue)


if __name__ == "__main__":
    T1 = Node(3)
    T2 = Node(9)
    T3 = Node(20)
    T4 = Node(15)
    T5 = Node(7)
    T1.left = T2
    T1.right = T3
    T3.left = T4
    T3.right = T5
    print(treeToDoublyList(T1))


