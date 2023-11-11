class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def count_live_neighbors(r, c):
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            return live_neighbors

        # Apply the rules of the game by modifying the board in-place
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is currently live but will die
                    board[r][c] = -1
                elif board[r][c] == 0 and live_neighbors == 3:
                    # 2 signifies the cell is currently dead but will live
                    board[r][c] = 2

        # Update the board to the next state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
