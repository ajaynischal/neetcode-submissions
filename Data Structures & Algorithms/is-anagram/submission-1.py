class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # hashset = set()
        # for i in s:
        #     hashset.add(i)
        
        # for i in t:
        #     if i in hashset:
        #         hashset.remove(i)
            
        # if len(hashset) == 0:
        #     return True
        
        # return False


        