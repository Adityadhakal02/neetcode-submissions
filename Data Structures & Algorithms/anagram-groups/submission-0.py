class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str in strs:
            key = ''.join(sorted(str))
            if key in anagrams:
                anagrams[key].append(str)
            else:
                anagrams[key] = [str]
        return list(anagrams.values())


        
        