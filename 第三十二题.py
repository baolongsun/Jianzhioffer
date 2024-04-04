# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    tag = 0
    deque = [root]
    res = []
    while deque:
        tmp = []
        for k in range(len(deque)):
            poped = deque.pop(0)
            if poped.left:
                deque.append(poped.left)
            if poped.right:
                deque.append(poped.right)
            if tag%2 == 0:
                tmp.append(poped.val)
            else:
                tmp.insert(0,poped.val)
        tag+=1
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