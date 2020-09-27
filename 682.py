#LeetCode problem 682: Baseball Game
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        prev=int(ops[0])
        res=[int(ops[0])]
        for i in range(1,len(ops)):
            if(ops[i]=="+" and len(res)>=2):
                res.append(res[-1]+res[-2])
            elif(ops[i]=="+" and len(res)<2):
                return 0
            elif(ops[i]=='C' and len(res)>=1):
                res.pop()
            elif(ops[i]=='C' and len(res)<1):
                return 0
            elif(ops[i]=='D' and len(res)>=1):
                res.append(2*res[-1])
            elif(ops[i]=='D' and len(res)<1):
                return 0
            try:
                res.append(int(ops[i]))
            except ValueError:
                continue
        return(sum(res))
            
            
            