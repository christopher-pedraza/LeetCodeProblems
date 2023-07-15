# Neetcode.io BRUTEFORCE solution
# Will Time Limit Exceed

# Time complexity: O(n^2)
# Space complexity: O(1)

def maxArea(height):
        res = 0

        for l in range(len(height)):
                for r in range(l+1, len(height)):
                        waterArea = (r-l) * min(height[l], height[r])
                        res = max(res, waterArea)

        return res
        
print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1
print(maxArea([0,2])) # 0
print(maxArea([2,3,4,5,18,17,6])) # 17
print(maxArea([1,3,2,5,25,24,5])) # 24