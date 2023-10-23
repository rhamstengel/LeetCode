class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index, step = 0, 1

        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(result)

# Example usage:
solution = Solution()
s1 = "PAYPALISHIRING"
numRows1 = 3
output1 = solution.convert(s1, numRows1)
print(output1)  # Output: "PAHNAPLSIIGYIR"
