class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gMap = {} # {'count': [words]}
        for word in strs: 
            count = [0] * 26 
            
            for ch in word: 
                count[ord(ch) - ord('a')] += 1 

            count = tuple(count)

            if count in gMap: 
                gMap[count].append(word)
            else: 
                gMap[count] = [word]
        return list(gMap.values())