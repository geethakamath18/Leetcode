#LeetCode problem 22: Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        def recursiveForm(s='', left=0, right=0):
            if len(s)==2*n:
                res.append(s)
                return
            if left<n:
                recursiveForm(s+'(',left+1,right)
            if right<left:
                recursiveForm(s+')',left,right+1)
        
        
        recursiveForm()
        return res
    
        
            
        
        
        