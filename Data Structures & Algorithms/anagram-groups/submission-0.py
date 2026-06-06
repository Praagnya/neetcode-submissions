class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gMap = {}
        for word in strs: 
            group = [0] * 26
            for ch in word: 
                group[ord(ch) - ord('a')] += 1

            group_add = tuple(group)

            if group_add in gMap: 
                gMap[group_add].append(word)
            else: 
                gMap[group_add] = [word]
        return list(gMap.values())
