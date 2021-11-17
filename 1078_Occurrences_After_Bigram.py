# LeetCode
# Level: Easy
# Date: 2021.11.17

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        S = text.split()
        
        n = 0
        a = []
        for i in S:
            n += 1
            if i == first and n < (len(S)-1):
                if S[n] == second:
                    a.append(S[n+1])
        return a