# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

#二叉苏搜索树，左边小于根节点，右边大于根节点
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def verifyPostorder(postorder):
    if not postorder:
        return True

    def f(postorder,i,j):
        if i >= j:#只有一个或0个元素
            return True
        root = postorder[j]
        p = i
        while postorder[p] < root:
            p+=1
        for k in range(p,j):
            if postorder[k] < root:
                return False
        return f(postorder,i,p-1) and f(postorder,p,j-1)

    return f(postorder,0,len(postorder)-1)

if __name__ == "__main__":
    print(verifyPostorder([1,3,2,6,5]))