# 二叉树的深度以及平衡二叉树
# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）
# 形成树的一条路径，最长路径的长度为树的深度。

# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

def isBalanced(root):
    if not root:
        return True
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return abs(right-left) <= 1 and isBalanced(root.left) and isBalanced(root.right)

if __name__ == "__main__":
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t5 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t4.left = t5
    print(maxDepth(t1))
    print(isBalanced(t1))