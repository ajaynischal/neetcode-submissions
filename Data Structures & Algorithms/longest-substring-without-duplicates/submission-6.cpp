class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> mp;
        int l = 0;
        int r = 0;
        int res = 0;

        while (r < s.size()) {
            while (mp.find(s[r]) != mp.end()) {
                mp.erase(s[l]);
                l++;
            }
            mp.insert(s[r]);
            r++;
            res = max(res, r-l);
        }
        return res; 
    }
};
