#LeetCode problem 454: 4Sum II
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        d={}
        for i in C:
            for j in D:
                s=i+j
                d[s]=d.get(s,0)+1

        for i in range(len(A)):
            for j in range(len(B)):
                target = 0-(A[i]+B[j])
                if target in d:
                    count+=d[target]
        return count