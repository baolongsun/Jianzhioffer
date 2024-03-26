class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#前序遍历 中左右
#中序遍历 左中右
#后序遍历 左右中
def preorderTraversal(root:TreeNode):
    if not root:
        return
    print(root.value)
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def inorderTraversal(root:TreeNode):
    if not root:
        return
    preorderTraversal(root.left)
    print(root.value)
    preorderTraversal(root.right)

def postorderTraversal(root:TreeNode):
    if not root:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.value)

if __name__  == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left = t2;t1.right = t3
    t3.left = t4
    preorderTraversal(t1);print('*'*10)
    inorderTraversal(t1);print('*'*10)
    postorderTraversal(t1);print('*'*10)

