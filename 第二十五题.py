# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# 镜像输出
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirrorTree(root):
    if not root or (not root.left and not root.right):
        return root
    left = mirrorTree(root.left)
    right = mirrorTree(root.right)
    root.left = right
    root.right = left
    return root

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    start = mirrorTree(t1)
    print(start.right.val)