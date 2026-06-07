class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums: 
            dic[i] = 1 + dic.get(i, 0)
        sort_dict = sorted(dic, key = dic.get, reverse=True)
        return sort_dict[:k]