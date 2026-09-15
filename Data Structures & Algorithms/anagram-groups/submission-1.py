class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            # append the actual string into an array of the key sortedString which
            # will allow grouping of all similar strings
            result[sortedString].append(string)
        return list(result.values())