class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Example
        ["app", "pap", "pay", "yap"] -> [["app", "pap"], ["pay", "yap"]]

        Solution
        1 - in a hashmap use tuple with character counts as keys and values as list of the strings
        2 - in a for loop for each string create an array of char count
        3 - after completing char count convert it to tuple as keys cannot be mutable
        4 - append the string to value array
        5 - return list(values)
        """
        anagrams = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            key = tuple(freq)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())