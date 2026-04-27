class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p = 1
        nums.sort()
        while nums:
            if p > len(nums)-1:
                break
            if nums[p] == nums[p-1]:
                return True
            
            p += 1
            
        return False

