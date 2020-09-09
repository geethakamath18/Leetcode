#LeetCode problem 54: Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(len(matrix)==0 or len(matrix[0])==0):
            return []
        res=[]
        rb=0
        re=len(matrix)
        cb=0
        ce=len(matrix[0])
        while(re>rb and ce>cb):
            for j in range(cb,ce):
                res.append(matrix[rb][j])
            for k in range(rb+1,re-1):
                res.append(matrix[k][ce-1])
            if(re!=rb+1):
                for l in range(ce-1,cb-1,-1):
                    res.append(matrix[re-1][l])
            if(cb!=ce-1):
                for m in range(re-2,rb,-1):
                    res.append(matrix[m][cb])
            rb+=1
            ce-=1
            cb+=1
            re-=1
        return(res)