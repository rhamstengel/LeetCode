class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                # Pop the top two elements from the stack
                a, b = stack.pop(), stack.pop()

                # Apply the operator and push the result back onto the stack
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    # Truncate towards zero for division
                    stack.append(int(b / a))
            else:
                # Push the operand onto the stack
                stack.append(int(token))

        return stack[0]
