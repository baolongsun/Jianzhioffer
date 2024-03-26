#重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#前序遍历的第一个点是根节点
#中序遍历的根节点左边是左子树,右边是右子树
#         3
#     9       20
# 5     6   15     7
#前序 (l1)3 9 5 6 20 15 7(r1)
#中序 (l2)5 9 6 3(i) 15 20 7(r2)
#因此子树为
# 中  [l2,i-1]  [i+1,r2]
# 前 [l1+1,l1+(i-l2)],[l1+(i-l2)+1,r1]
#在中序遍历中通过遍历找到root的index
from tree import TreeNode

def buildTree(preorder,inorder):
    map = {}
    for i in range(len(inorder)):
        map[inorder[i]] = i
    def f(preorder,l1,r1,inorder,l2,r2):
        if l1>r1 or l2>r2:
            return None
        root = TreeNode(preorder[l1])
        i = map[preorder[l1]]
        root.left = f(preorder,l1+1,l1+i-l2,inorder,l2,i-1)
        root.right = f(preorder,l1+i-l2+1,r1,inorder,i+1,r2)
        return root
    return f(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

if __name__ == "__main__":
    preorder = [3,9,20,15,7];inorder = [9,3,15,20,7]
    root = buildTree(preorder,inorder)
    a = 2


