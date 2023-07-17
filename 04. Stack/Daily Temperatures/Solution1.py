# Neetcode.io solution

# Time complexity: O(n)  - iterate once over the list
# Space complexity: O(n) - need a stack

def dailyTemperatures(temperatures: list[int]) -> list[int]:
	# Will store the temperatures and their index
	# For each temperature in the list, I will check the top
	# temperature and see if it's smaller. If it's, I'll get
	# the difference of the indexes, which will be the amount
	# of days needed to get a higher temperature. I will keep
	# checking until the temperature at the top is greater or
	# equal than the new temperature. If so, I will just add
	# the new temperature to the top of the stack
	# Contains pairs: (temperature, index)
	stack = [] 
	# Output list, contains 0s as default value in case I don't
	# find a day with greater temperature than current, I can
	# keep the 0. The size needs to be the same as the input
	# array
	res = [0]*len(temperatures)

	# Iterate over the temperatures getting the value and index
	for i, temp in enumerate(temperatures):
		# In the first cycle, the stack will be empty, thus, this
		# loop won't run. However, if the stack isn't empty keep
		# getting the amounts of days it takes to get a greater
		# temperature, while the current temperature is greater
		# than the one at the top of the stack.
		# In python there isn't a top() function, so we access
		# the last element with the negative index "-1"
		# The second index refers to the elements of the pair
		# Index 
		while stack and stack[-1][0] < temp:
			topTemp = stack.pop()
			res[topTemp[1]] = i - topTemp[1]

		# Append to the stack the current temperature and its index
		stack.append((temp, i))

	return res


print(dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(dailyTemperatures([30,60,90])) # [1,1,0]
print(dailyTemperatures([99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 100])) # [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]