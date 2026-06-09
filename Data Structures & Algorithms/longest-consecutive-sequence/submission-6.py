class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums: 
            current = i 
            if (i-1) in nums_set: 
                continue 
            length = 1
            while current + 1 in nums_set: 
                length += 1 
                current += 1 
            longest = max(longest, length)
            print(longest)
        return longest