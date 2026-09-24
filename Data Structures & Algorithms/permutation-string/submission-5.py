class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = Counter(s1)
        needed = len(s1Count)
        windowCount = defaultdict(int)

        for i in range(len(s1)):
            if s2[i] in s1Count:
                windowCount[s2[i]] +=1

        # add 1 for each char in s1Count, if char count in window matches is s1Count
        matches = sum(1 for ch in s1Count if s1Count[ch] == windowCount.get(ch,0)) 
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == needed:
                return True
            
            charToAdd = s2[r]
            if charToAdd in s1Count:
                windowCount[charToAdd] +=1
                if windowCount[charToAdd] == s1Count[charToAdd]:
                    matches +=1
                elif windowCount[charToAdd] == s1Count[charToAdd] + 1:
                    matches -=1

            charToRemove = s2[l]
            if charToRemove in s1Count:
                windowCount[charToRemove] -=1
                if windowCount[charToRemove] == s1Count[charToRemove]:
                    matches +=1
                elif windowCount[charToRemove] == s1Count[charToRemove] - 1:
                    matches -=1
            l += 1

        return matches == needed