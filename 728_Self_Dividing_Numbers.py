# LeetCode
# Level: Easy
# Date: 2021.11.05

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        A = []
        for i in range(left,right+1):
            n = 0
            L = list(str(i))
            if "0" in L:
                continue
            for j in range(len(L)):
                if i % int(L[j]) == 0:
                    n += 1
                if n == len(L):
                    A.append(i)
        return A



