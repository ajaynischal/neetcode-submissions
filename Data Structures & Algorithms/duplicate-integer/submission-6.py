class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupp = {}
        for i, n in enumerate(nums):
            if n in dupp:
                return True
            dupp[n] = i
        
        return False
         