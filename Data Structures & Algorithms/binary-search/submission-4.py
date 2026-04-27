import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        
        # Check if the target exists at the found index
        if index < len(nums) and nums[index] == target:
            return index
        return -1




        