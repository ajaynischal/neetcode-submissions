class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            char[ord(s[i]) - ord('a')] += 1
            char[ord(t[i]) - ord('a')] -= 1 
        
        for val in char:
            if val != 0:
                return False
        
        return True
            
        
