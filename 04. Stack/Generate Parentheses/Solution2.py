# Time complexity: O(n^2)??? - Iterate 2n and for each iteration
#                              iterate over the entire stack
# Space complexity: O(n) - Need a stack

def generateParenthesis(n: int) -> list[str]:
	# Stack containing dictionary with the parentheses combination
	# and the opening and closing parentheses count
	stack = [{"comb":"(", "opCount":1, "clCount":0}]
	# Resulting list
	res = []

	# iterate over n opening parentheses and n closing parentheses
	for i in range(2*n):
		# Iterate over the elements in the stack
		for j in range(len(stack)):
			# If the length of the current combination is lower than
			# i, which goes from 0 to 2n (n opening parentheses and
			# n closing parenthesese), then it means that the
			# combination will no longer be valid so we pop it from
			# the stack
			if len(stack[j]["comb"]) < i:
				stack.pop(j)
				continue

			# If the last char in the combination is an opening
			# parenthesis, the opening parentheses count is lower
			# or equal than n, as well as greater than the closing
			# parentheses count, we add a closing parenthesis
			if (stack[j]["comb"][-1] == "(" and
				stack[j]["opCount"] <= n and
				stack[j]["opCount"] > stack[j]["clCount"]):
				# Add closing parenthesis to the combination
				combination = stack[j]["comb"] + ")"
				# Append to the stack the new combination
				stack.append({"comb":combination,
					"opCount":stack[j]["opCount"],
					"clCount":stack[j]["clCount"]+1})

			# If the last char is an opening parenthesis and the
			# opening count is lower than n, we can add an opening
			# parenthesis
			if (stack[j]["comb"][-1] == "(" and
				stack[j]["opCount"] < n):
				# Add opening parenthesis
				combination = stack[j]["comb"] + "("
				# Update the current position of the stack
				stack[j]["comb"] = combination
				stack[j]["opCount"] += 1

			# If the last char is a closing parenthesis and the
			# closing count is lower than the opening count as well
			# as n, we add a closing parenthesis
			if (stack[j]["comb"][-1] == ")" and
				stack[j]["clCount"] < stack[j]["opCount"] and
				stack[j]["clCount"] < n):
				# Add closing parenthesis to the combination
				combination = stack[j]["comb"] + ")"
				# Append to the stack the new combination
				stack.append({"comb":combination,
					"opCount":stack[j]["opCount"],
					"clCount":stack[j]["clCount"]+1})

			# If the last char is a closing parenthesis and the
			# opening count is still lower than n, we add an
			# opening parenthesis
			if (stack[j]["comb"][-1] == ")" and
				stack[j]["opCount"] < n):
				# Add opening parenthesis
				combination = stack[j]["comb"] + "("
				# Update the current position of the stack
				stack[j]["comb"] = combination
				stack[j]["opCount"] += 1

	# Iterate over the stack getting the combinations into res
	# that have the correct length of 2n avoiding repetitive
	# values
	for s in stack:
		if (s["comb"] not in res and
			len(s["comb"]) == 2*n):
			res.append(s["comb"])

	# Return the valid combinations of parentheses
	return res

print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1)) # ["()"]
print(generateParenthesis(8)) # Very long