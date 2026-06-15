class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {} # char: index 
        res = 0 
        l = 0 
        for r in range(len(s)): 
            if s[r] in count: 
                l = max(count[s[r]] + 1, l)
            count[s[r]] = r
            res = max(res, r - l + 1)
        return res 
             
