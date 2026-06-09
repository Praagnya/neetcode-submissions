class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # ASCII -> List[Anagram]
        for i in strs: 
            count = [0] * 26
            for ch in i: 
                count[ord(ch) - ord('a')] += 1 
                
            count_tuple = tuple(count)
            if count_tuple in map: 
                map[count_tuple].append(i)
            else:
                map[count_tuple] = [i]
        
        return list(map.values())