#LeetCode problem 26: Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums) -> int:
        num = int
        remove = []
        for i,j in enumerate(nums):
            if j == num:
                remove.append(i)
                continue
            num = j
        for i in reversed(remove):
            nums.pop(i)   
        return len(nums)

x=Solution()
l1=[1,1,2]
print(x.removeDuplicates(l1))

