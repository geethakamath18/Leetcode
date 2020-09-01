#LeetCode problem 283: Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c+=1
            else:
                continue
        for i in range(c):
            nums.remove(0)
        nums+=[0]*c
        