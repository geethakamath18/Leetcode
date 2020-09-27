#LeetCode problem 387: First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if(len(s)==0):
            return -1
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        i=0
        dv=list(d.values())
        dk=list(d.keys())
        for i in range(len(dv)):
            if(dv[i]==1):
                return s.index(dk[i])
        return -1
        