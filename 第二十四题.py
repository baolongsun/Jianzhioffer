# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubStructure(A,B):
    if A == None or B == None:
        return
    if isSubTree(A,B):
        return True
    if isSubStructure(A.left,B) or isSubStructure(A.right,B):#递归
        return True
    return False

def isSubTree(Ta,Tb):
    if Tb is None:
        return True
    if Ta is None:
        return False
    if Ta.val != Tb.val:
        return False
    return isSubTree(Ta.left,Tb.left) and isSubTree(Ta.right,Tb.right)

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(1)
    t6 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t3.left = t4

    t5.left = t6
    print(isSubStructure(t1,t5))

