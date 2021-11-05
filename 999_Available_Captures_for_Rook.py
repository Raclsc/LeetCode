# LeetCode
# Level: Easy
# Date: 2021.11.3

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(len(board)):
            if "R" in board[i]:
                j = board[i].index("R")
                break
        
        n = 0
        for k in range(i,-1,-1):
            if board[k][j] == "B":
                break
            elif board[k][j] == "p":
                n += 1
                break
        
        for k in range(j,-1,-1):
            if board[i][k] == "B":
                break
            elif board[i][k] == "p":
                n += 1
                break
        
        for k in range(i,len(board)):
            if board[k][j] == "B":
                break
            elif board[k][j] == "p":
                n += 1
                break
        
        for k in range(j,len(board[i])):
            if board[i][k] == "B":
                break
            elif board[i][k] == "p":
                n += 1
                break
                    
        return n