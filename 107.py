#LeetCode problem 107: Binary Tree Level Order Traversal II
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        d=self.getDepth(root)
        result=[]
        for i in range(1,d+1):
            a=[]
            self.printNodes(root,a,i)
            print("a:",a,"level:",i)
            result.append(a)
        return result[::-1]
    
    def printNodes(self, root: TreeNode,a,level)->List[int]:
        if root is None:
            return
        if level==1:
            a.append(root.val)
        else:
            self.printNodes(root.left,a,level-1)
            self.printNodes(root.right,a,level-1)
    
    def getDepth(self,root: TreeNode)->int:
        if root is None:
            return 0
        l=self.getDepth(root.left)
        r=self.getDepth(root.right)
        if l>r: return l+1
        else: return r+1