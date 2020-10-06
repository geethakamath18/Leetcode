#LeetCode problem 448: Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        if len(nums)==0:
            return []
        l=len(nums)
        nums=set(nums)
        for i in range(1,l+1):
            if i not in nums:
                res.append(i)
        return res