#LeetCode problem 429: N-ary Tree Level Order Traversal 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        h=self.getHeight(root)
        for i in range(1,h+1):
            a=[]
            self.getLevelOrder(root,a,i)
            res.append(a)
        return res
        
    def getHeight(self, root:'Node')->int:
        if root is None:
            return 0
        m=1
        for child in root.children:
            m=max(self.getHeight(child)+1,m)
        return m
        
    def getLevelOrder(self, root: 'Node', l:List, level:int):
        if level==1:
            l.append(root.val)
        for child in root.children:
            self.getLevelOrder(child,l,level-1)
