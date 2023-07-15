class MinStack:
    # Constructor
    # Time complexity: O(1)
    def __init__(self):
        # Empty stack to store the numbers
        self.stack = []
        # The min value starts as positive infinite
        # because any other number should be less than
        # it so it gets replaced
        self.minVal = float("inf")

    # Appends to the top of the stack a number
    # Time complexity: O(1)
    def push(self, val: int) -> None:
        # Add to the end of the stack the new value
        self.stack += [val]
        # If the new value is less than the current minimum,
        # replace the minimum with the current value
        if val < self.minVal:
            self.minVal = val

    # Removes from the top of the stack a number
    # Time complexity: O(n) - finding the new min could need
    #                         to iterate over the entire list
    def pop(self) -> None:
        # If the top number of the stack that is going to be
        # removed is the minimum and the stack won't be empty
        # after removing it (meaning it only had 1 number)
        # Replace the current min with the new min from the
        # stack
        if self.stack[-1] == self.minVal and self.stack[:-1]:
            self.minVal = min(self.stack[:-1])
        # If the stack will be empty after removing the number
        # just replace the min with a positive infinite so the
        # next number it receives becomes the new min
        elif not self.stack[:-1]:
            self.minVal = float("inf")
        # If the last number of the stack is not the min or the
        # stack will become empty, don't do anything with the min
        # and just remove the last value
        self.stack = self.stack[:-1]

    # Peeks at the top value from the stack
    # Time complexity: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Returns the minimum value saved in the stack
    # Time complexity: O(1)
    def getMin(self) -> int:
        # Returns the minimum if it isn't a positive infinite
        # (meaning the stack is empty. Could also check `if not
        # stack` to see if the stack is empty instead of checking
        # for the min), if it is, return none
        return self.minVal if self.minVal != float("inf") else None

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.stack)
print(obj.getMin())