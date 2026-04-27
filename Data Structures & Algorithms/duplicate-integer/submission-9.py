class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}

        for i in range(len(nums)):
            if nums[i] in dupe:
                return True
            dupe[nums[i]] = i

        return False 

    


            
