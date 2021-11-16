# LeetCode
# Level: Easy
# Date: 2021.11.16

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        
        deep = 0
                
        for child in root.children:
            deep = max(deep, self.maxDepth(child))
            print(deep)     
        
        print(root.val, "/", deep)
        
        return deep + 1