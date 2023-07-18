# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(n) - Need a stack

# RULES:
# Add open parenthesis if openCount < n
# Add closing parenthesis if closeCount < open
# Valid if openCount == closeCount == n

def generateParenthesis(n: int) -> list[str]:
    # Will hold the parenthesis
    stack = []
    # List of valid parentheses combinations
    res = []

    # Nested function so we don't need to pass
    # n. This function will be called recursively
    # while adding parenthesis
    def backtrack(openN, closedN):
        # If we have the same amount of opening and
        # closing parentheses, and these counts equal
        # n, then we are finished
        if openN == closedN == n:
            # Takes all the characters in the stack
            # (the parentheses) and joins them together
            # into an empty string. This string is
            # appended to the result list
            res.append("".join(stack))
            # As we already have the necessary parentheses
            # we return so this recursive thread stops
            return

        # If the open count is less than n
        if openN < n:
            # Add to the stack an opening parenthesis
            stack.append("(")
            # Call the function updating the counts
            backtrack(openN + 1, closedN)
            # As we only have 1 stack, everytime the function
            # returns, we will pop the character we just added
            # Basically, when we get to the first condition
            # we start returning to each of the calls and
            # popping the parentheses we added so we can create
            # another combination
            stack.pop()

        # If the closed count is less than the open count
        if closedN < openN:
            # Add to the stack an closing parenthesis
            stack.append(")")
            # Call the function updating the counts
            backtrack(openN, closedN + 1)
            # Remove the char we just added
            stack.pop()

    # Beginning of the backtracking. At the beginning both
    # of the counts are 0
    backtrack(0, 0)

    # Return the resulting list with the parentheses' combinations
    return res

print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1)) # ["()"]
print(generateParenthesis(8)) # Very long