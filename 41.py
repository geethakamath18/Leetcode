#LeetCode problem 41: First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 1
        if(max(nums)<0):
            return 1
        for i in range(1,max(nums)+2):
            if i in nums:
                continue
            return i