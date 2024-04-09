# 二叉树的深度
# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）
# 形成树的一条路径，最长路径的长度为树的深度。


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

if __name__ == "__main__":
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    print(maxDepth(t1))