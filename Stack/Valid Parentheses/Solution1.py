# Neetcode.io solution

# Less intuitive than mine, but overall, pretty
# much the same but in a different order and
# using a Hash Map instead of a list (in mine,
# I look in a list, but that would be O(3), 
# technically the same time complexity for
# lookup)

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

	# Dict with the closing parentheses as a key
	# and opening as the value that will help to
	# check if the parenthesis was closed
	# correctly
	parenthesesMatch = {")":"(", "]":"[", "}":"{"}

	for p in s:
		# If the current parenthesis is a closing
		# parenthesis
		if p in parenthesesMatch:
			# If the stack is not empty and the last value
			# from it is the matching opening parenthesis
			# for the current parenthesis `p`, remove it
			# from the stack
			if stack and stack[-1] == parenthesesMatch[p]:
				stack.pop()
			# If they don't match or the stack is empty,
			# it means it's not valid
			else:
				return False
		# Add to the stack if it's an opening parenthesis
		else:
			stack.append(p)

	# Return True if the stack is empty (you have closed
	# all parentheses) and didn't find any invalid one
	# in the process
	return True if not stack else False

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
# DON'T FORGET TO CHECK FOR EDGE CASES!!!!
print(isValid("[")) # False
print(isValid("]")) # False