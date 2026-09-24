class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        windowCount = defaultdict(int) 

        for i in range(len(s1)):
            if s2[i] in s1Count:
                windowCount[s2[i]] += 1

        matches = sum(1 for ch in s1Count if s1Count[ch] == windowCount.get(ch, 0))
        needed = len(s1Count)   # number of *distinct* letters in s1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True

            add_ch = s2[r]
            if add_ch in s1Count:
                windowCount[add_ch] += 1
                if windowCount[add_ch] == s1Count[add_ch]:
                    matches += 1
                elif windowCount[add_ch] == s1Count[add_ch] + 1:
                    matches -= 1

            remove_ch = s2[l]
            if remove_ch in s1Count:
                windowCount[remove_ch] -= 1
                if windowCount[remove_ch] == s1Count[remove_ch]:
                    matches += 1
                elif windowCount[remove_ch] == s1Count[remove_ch] - 1:
                    matches -= 1
            l += 1

        return matches == needed        