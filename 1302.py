#LeetCode problem 1302: Deepest Leaves Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        #h=self.height(root)
        res=[]
        for i in range(1,self.height(root)+1):
            a=[]
            self.returnSum(root, i,a)
            res.append(a)
        return(sum(res[len(res)-1]))
        
    def height(self, root: TreeNode)->int:
        if root is None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        if l>=r:
            return l+1
        return r+1
     
    def returnSum(self, root: TreeNode,level: int,a: int):
        if root is None:
            return
        if level==1:
            a.append(root.val)
        else:
            self.returnSum(root.left,level-1,a)
            self.returnSum(root.right,level-1,a)
            
        