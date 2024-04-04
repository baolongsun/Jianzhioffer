# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。

#采用深度优先做法

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root,target):
    res = []
    tmp = []
    def dsf(root,target):
        if not root:
            return
        tmp.append(root.val)
        target -= root.val
        if not root.left and not root.right and target == 0:
            res.append(tmp[:])
        dsf(root.left,target)
        dsf(root.right,target)
        tmp.pop()
    dsf(root,target)
    return res
if __name__ == "__main__":
    T1 = TreeNode(1)
    T2 = TreeNode(2)
    T3 = TreeNode(3)
    T1.left = T2
    T1.right = T3
    print(pathSum(T1,4))