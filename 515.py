#LeetCode problem 515: Find Largest Value in Each Tree Row
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        h=self.getHeight(root)
        res=[]
        for i in range(1,h+1):
            ans=[]
            self.getLevelOrder(root,i,ans)
            res.append(max(ans))
        # finalres=[]
        # for i in res:
        #     finalres.append(max(i))
        return res
    
    def getHeight(self,root:TreeNode)->int:
        if root is None:
            return 0
        l=self.getHeight(root.left)
        r=self.getHeight(root.right)
        if l>=r:
            return l+1
        else:
            return r+1
    
    def getLevelOrder(self, root: TreeNode, level, ans):
        if root is None:
            return
        if(level==1):
            ans.append(root.val)
        else:
            self.getLevelOrder(root.left,level-1,ans)
            self.getLevelOrder(root.right,level-1,ans)
            