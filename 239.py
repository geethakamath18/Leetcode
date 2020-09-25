#LeetCode problem 239: Sliding Window Maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        q=[]
        res=[]
        res.append(max(nums[:k]))
        for i in range(len(nums)):
            
            if q and q[0]<i-k+1:
                q.pop(0)
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if i>=k:
                res.append(nums[q[0]])
        return res