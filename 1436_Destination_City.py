# LeetCode
# Level: Easy
# Date: 2021.11.17

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
    
        P = dict(paths)
        PA = P.keys()
        PB = P.values()
        
        DC = PB - PA
        
        for i in DC:
            return(i)