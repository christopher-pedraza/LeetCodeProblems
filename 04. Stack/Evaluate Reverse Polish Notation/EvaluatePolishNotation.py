# Own version in order to test if I understood
# correctly the evaluation of reverse polish
# notation problem

# Time complexity: O(n)
# Space complexity: O(n)

def evalPN(tokens: list[str]) -> int:
    # We will be storing the numbers and results we
    # get from the operations in a stack. As the
    # operators are always on the left, we know
    # that if we go through the list of tokens from
    # right to left, we will have the necessary
    # values by the time we get to an operator. And
    # when we get to it, we just need to pop the
    # last 2 values as we have already calculated 
    # any operation regarding them
    stack = []

    # Iterate over the tokens from right to left
    for i in range(len(tokens)-1, -1, -1):
        c = tokens[i]
        # Check for the operators
        # If it's an addition, we take the last 2
        # values and add them together. Then we add
        # to the top of the stack the result
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        # If it's a substraction, we take the last 2
        # values and substract them together. Then we
        # add to the top of the stack the result.
        # However, it's important to notice that we
        # should substract the last value from the
        # previous to last. Thus, we first pop both
        # and then substract the previous to last 
        # from the last one
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        # If it's a multiplication, we take the last 2
        # values and multiply them together. Then we 
        # add to the top of the stack the result
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        # If it's a division, we take the last 2
        # values and divide them together. Then we
        # add to the top of the stack the result.
        # However, it's important to notice that we
        # should divide the last value from the
        # previous to last. Thus, we first pop both
        # and then divide the previous to last 
        # from the last one
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))

        # If the char is not an operator, it means it
        # is a number, so we add it to the stack as an
        # int
        else:
            stack.append(int(c))

    # At the end the stack should only have 1 value which
    # is the result of the operation. There's always 1
    # solution so we know that it will be on the index 0
    return stack[0]

print(evalPN(["*","3","+","1","2"])) # 9
print(evalPN(["+","/","5","13","4"])) # 6
print(evalPN(["+","5","+","17","*","/","*","-11","+","3","9","6","10"])) # 22