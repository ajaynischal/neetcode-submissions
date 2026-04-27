class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset initialization
        hashset = set()
        
        # for loop to iterate through nums until no more numbers return false and terminate
        for n in nums:
            #check if it is in the hash
            if n in hashset:
                return True
            # add to hashset 
            hashset.add(n)

        return False


         