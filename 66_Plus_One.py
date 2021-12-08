# LeetCode
# Level: Easy
# Date: 2021.12.8

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        
        for i in range(len(digits), 0, -1):
            num = num + 10**(i-1)*digits[-i]
        
        num = list(str(num + 1))
        
        for i in range(len(num)):
            num[i] = int(num[i])
        
        return num