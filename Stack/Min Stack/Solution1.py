# Neetcode.io solution

# Trick: have another stack that contains the
# current min from the previous numbers pushed
# or if the new number is the new min, that has
# that. In general, a stack that for every
# position, it contains what is the minimum
# value up to that position

class MinStack:
    # Constructor
    # Time complexity: O(1)
    def __init__(self):
        # Stack of the numbers that are pushed
        self.stack = []
        # Stack that contains the minimum value for
        # each of the cells in the stack. For ex:
        # Stack     MinimumStack
        #   2           -10
        #   15          -10
        #  -10          -10
        #   5            2
        #   2            2
        #   10           4
        #   4            4
        #   9            9
        self.minStack = []

    # Appends to the top of the stack a number
    # Time complexity: O(1)
    def push(self, val: int) -> None:
        # Add to the stack the new value
        self.stack.append(val)
        # Get the minimum from the last nubmer in the minStack and
        # the received value. If the received value is less than
        # the min of the last index, for this new position you are
        # going to use the received value as the min in the minStack
        # However, if it is greater, you are still going to use the
        # previous min for this index
        # Also check if the minStack is empty or not. If it's empty,
        # just use the received value
        val = min(val, self.minStack[-1] if self.minStack else val)
        # Add the calculated min to the minStack
        self.minStack.append(val)

    # Removes from the top of the stack a number
    # Time complexity: O(1)
    def pop(self) -> None:
        # Remove the top number
        self.stack.pop()
        # Remove the min value for that number
        self.minStack.pop()

    # Peeks at the top value from the stack
    # Time complexity: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Returns the top value saved in the min stack
    # Time complexity: O(1)
    def getMin(self) -> int:
        return self.minStack[-1]

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