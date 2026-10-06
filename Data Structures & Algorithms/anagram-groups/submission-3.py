class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedKeys = ["".join(sorted(string)) for string in strs]
        sortedKeysMap = {key: [] for key in sortedKeys}
        for strKey in strs:
            sorted_str = "".join(sorted(strKey))
            sortedKeysMap.get(sorted_str).append(strKey)
            
        return [v for k,v in sortedKeysMap.items()]
        
            