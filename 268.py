#LeetCode problem 268: Missing Number
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,max(nums)+2):
            if i not in nums:
                return i