class MinStack:

    def __init__(self):
        # Main stack to store the elements
        self.stack = []
        # Stack to store the minimum elements
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the min stack is empty or the new value is smaller than the current minimum,
        # push it onto the min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the top element is the same as the current minimum, pop it from the min stack
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The current minimum is the top element of the min stack
        return self.min_stack[-1]
