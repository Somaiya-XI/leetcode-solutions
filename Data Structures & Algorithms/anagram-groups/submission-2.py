class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for string in strs:
            s = ''.join(sorted(string))
            group[s].append(string)
            
        return list(group.values())