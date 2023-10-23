from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)

        # Check each column
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)

        # Check each 3x3 sub-box
        for i in range(3):
            for j in range(3):
                seen = set()
                for row in range(3 * i, 3 * i + 3):
                    for col in range(3 * j, 3 * j + 3):
                        cell = board[row][col]
                        if cell != '.':
                            if cell in seen:
                                return False
                            seen.add(cell)

        return True
