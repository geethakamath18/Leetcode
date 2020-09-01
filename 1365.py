#LeetCode problem 1365: How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        a={}
        for i in sorted(nums):
            d[i]=d.get(i,0)+1
        v=list(d.values())
        k=list(d.keys())
        res=[0]
        for i in range(1,len(v)):
            res.append(res[-1]+v[i-1])
        j=0
        for i in k:
            a[i]=res[j]
            j+=1
        res=[]
        for l in nums:
            res.append(a.get(l))
        return res