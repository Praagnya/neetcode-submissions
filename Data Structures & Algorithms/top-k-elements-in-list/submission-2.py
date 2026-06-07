class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # 
        bucket = [[] for _ in range(len(nums) + 1)]
        for i in nums: 
            map[i] = 1 + map.get(i, 0)
        for num, cnt in map.items(): 
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]: 
                res.append(num)
                if len(res) == k: 
                    return res