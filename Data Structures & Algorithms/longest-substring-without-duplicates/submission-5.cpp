class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        //hashmap 
        // x y z
        // count = 3
        // res = max(res, 3) = 3
        unordered_set<char> dupe; //dupe = {}
        int l = 0;
        int r = 0;
        int res = 0;

        while (r < s.size()) {
            while (dupe.find(s[r]) != dupe.end()) { // if s[r] in dupe: 
                dupe.erase(s[l]);
                l++;
            }
            dupe.insert(s[r]);
            r++;
            res = max(res, r - l);
            //xyzz

        }
        return res;
        
    }
};
