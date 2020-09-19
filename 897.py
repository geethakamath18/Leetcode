#LeetCode problem 897: Increasing Order Search Tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res=[]
        if root.left is None and root.right is None:
            return TreeNode(root.val)
        res=self.getPreOrder(root,res)
        a=None
        a=newNode=TreeNode(res[0])
        for i in range(1,len(res)):
            newNode.right=TreeNode(res[i])
            newNode=newNode.right
        return a
    
    def getPreOrder(self, root: TreeNode,r)->List[int]:
        if root is None:
            return
        self.getPreOrder(root.left,r)
        r.append(root.val)
        self.getPreOrder(root.right,r)
        return r