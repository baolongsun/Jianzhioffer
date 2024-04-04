# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    queue = [root]
    res = []

    while queue:
        k = len(queue)
        tmp = []
        for i in range(k):
            poped = queue.pop(0)
            if poped.left:
                queue.append(poped.left)
            if poped.right:
                queue.append(poped.right)
            tmp.append(poped.val)
        res.append(tmp)
    return res

if __name__ == "__main__":
    T1 = TreeNode(3)
    T2 = TreeNode(9)
    T3 = TreeNode(20)
    T4 = TreeNode(15)
    T5 = TreeNode(7)
    T1.left = T2
    T1.right = T3
    T3.left = T4
    T3.right = T5
    print(levelOrder(T1))