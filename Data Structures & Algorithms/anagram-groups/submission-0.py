class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #res = {} #mapping charCount to list of Anagrams
        for s in strs:
            count= [0]*26 # a...z but rn it is 26 0s

            for c in s:
                # this will calculate the a to index 0 using ascii
                count[ord(c)-ord("a")] += 1 #counting each character

            # we want to append but if it doesnt exist yet so we will change to default dict(list) to get rid of edgecase 
            res[tuple(count)].append(s) # python cannot have keys so we will change it to a tuple as it is unmmutable
        
        return res.values()