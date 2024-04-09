# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
#二叉搜索树的中序遍历为从小到大顺序,为左,根,右

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.target = 0

    def kthLargest(self,root,k):
        self.k = k
        if not root:
            return
        self.midFind(root)
        return self.target

    def midFind(self,root):
        if not root or self.k <= 0:
            return
        self.midFind(root.right)
        self.k -= 1
        if self.k == 0:
            self.target = root.val
        self.midFind(root.left)

if __name__ == "__main__":
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    q = Solution()
    print(q.kthLargest(t1,1))















