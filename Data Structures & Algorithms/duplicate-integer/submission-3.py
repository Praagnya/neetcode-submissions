class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums: 
            seen.add(i)
        if len(nums) == len(seen):
            return False
        return True 