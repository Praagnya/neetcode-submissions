class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target: 
                    return [i, j]
        return []      
        
        # nMap = {}
        # for i, j in enumerate(nums):
        #     diff = target - j  
        #     if diff in nMap: 
        #         return [nMap[diff], i]
        #     nMap[j] = i