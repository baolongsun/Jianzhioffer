# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def f(A,B):
    if not A and not B:
        return True
    if not A or not B:
        return False
    if A.val != B.val:
        return False
    return f(A.left,B.right) and f(A.right,B.left)

def isSymmetric(root):
    if not root or (not root.left and not root.right):
        return True
    return f(root.left,root.right)



if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    print(isSymmetric(t1))