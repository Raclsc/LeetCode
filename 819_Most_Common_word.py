# LeetCode
# Level: Easy
# Date: 2021.11.09

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        sample = ",.!?;'"
        for i in sample:
            paragraph = paragraph.replace(i," ")
       
        S = paragraph.lower().split()

        for i in range(len(banned)):
            while banned[i] in S:
                S.remove(banned[i])

        d = {}
        for i in S:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        n = 0
        for key, value in d.items():
            if value > n:
                ans = key
                n = value
        return ans