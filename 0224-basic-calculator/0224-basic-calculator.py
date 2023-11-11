class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                result += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                result += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                # Push the result and sign onto the stack, for later
                # Reset the sign and result for the new sub-expression
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ch == ')':
                # Add the sub-expression result inside the parentheses
                result += sign * operand
                result *= stack.pop()  # stack.pop() is the sign before the parentheses
                result += stack.pop()  # stack.pop() now is the result calculated before the parentheses
                operand = 0

        return result + sign * operand
