class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Determine if the first row or first column need to be zeroed
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # Use first row and column to mark zero rows and columns
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # Zero out cells based on marks in the first row and column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the first row and column if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
