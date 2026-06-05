class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        for i, j in enumerate(nums):
            diff = target - j  
            if diff in nMap: 
                return [nMap[diff], i]
            nMap[j] = i