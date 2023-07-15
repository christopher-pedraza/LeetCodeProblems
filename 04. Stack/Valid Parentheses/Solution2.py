# Time complexity: O(n) - iterate once over the
#						  string
# Space complexity: O(n) - worst case scenario,
#						   you only have opening
#						   parentheses and the
#						   stack is of size n

def isValid(s):
	# Add the opening parentheses to the stack
	# Pop when you find a closing one
	# Check if current closing one match with
	# the popped parenthesis
	stack = []

	for p in s:
		# If it's an opening parenthesis add it
		# to the stack
		if p in ["(", "[", "{"]:
			stack.append(p)
		# If it's a closing one, pop and check
		# if they match
		else:
			# If you got a closing parenthesis and
			# the stack is empty, it means it's
			# not valid
			if not stack:
				return False

			# Get the parenthesis in the top of
			# the stack and remove it from the
			# stack
			current = stack.pop()
			# If the current parenthesis doesn't 
			# match with the popped one, return
			# false
			if (current == "(" and p != ")" or
				current == "[" and p != "]" or
				current == "{" and p != "}"):
				return False

	# If you never found an invalid parenthesis
	# and the stack is empty, return true
	return (True if not stack else False)

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
# DON'T FORGET TO CHECK FOR EDGE CASES!!!!
print(isValid("[")) # False
print(isValid("]")) # False