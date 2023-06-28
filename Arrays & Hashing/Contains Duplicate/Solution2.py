# Time complexity: O(n) - convert list to set
# Space complexity: O(n) - because you need a hashset of size n

def containsDuplicate(nums):
    return (len(set(nums))<len(nums))

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))