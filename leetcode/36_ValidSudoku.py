# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

from typing import List

class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Runtime: 112 ms, faster than 22.03% of Python3 online submissions for Valid Sudoku.
        # Memory Usage: 14.4 MB, less than 40.35% of Python3 online submissions for Valid Sudoku.
        def valid(nums):
            has = []
            for n in nums:
                if n !='.':
                    if n in has:
                        return False
                    else:
                        has.append(n)
        # Runtime: 100 ms, faster than 51.10% of Python3 online submissions for Valid Sudoku.
        # Memory Usage: 14.1 MB, less than 88.09% of Python3 online submissions for Valid Sudoku.
        def valid_hash(nums):
            has = set()
            for n in nums:
                if n !='.':
                    if n in has:
                        return False
                    else:
                        has.add(n)
        
        for r in board:
            if valid(r) is False:
                return False
        
        for i in range(9):
            c = [board[j][i] for j in range(9)]
            
            if valid(c) is False:
                return False
        
        for x in range(3):
            for y in range(3):
                rx = x*3
                ry = y*3
                c = board[rx][ry:ry+3] + board[rx+1][ry:ry+3] + board[rx+2][ry:ry+3]
                print(c)
                if valid(c) is False:
                    return False

        return True

s = Solution()
print(s.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))