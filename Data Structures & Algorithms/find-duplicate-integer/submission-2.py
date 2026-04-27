class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicates = set()
        for i in range(len(nums)):
            if nums[i] in duplicates:
                return nums[i]
            duplicates.add(nums[i])
        


        