class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string  
            # ["Hi", "there"] -> "2#Hi5#there"
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            length = int(s[i:j]) 
            # if we reach the bound characted meaning from current i till the j when
            # reached # that is the length e,g. 143
            result.append(s[j + 1 : j + 1 + length])  
            # 2#Hi5#there -> s[0] = 2, s[j=1] = # s[0:1] 
            # -> length = 2, s[1 +1: 1+1+2] = s[2:4] -> "Hi" index 2 & 3
            i =  j + 1 + length
        return result
