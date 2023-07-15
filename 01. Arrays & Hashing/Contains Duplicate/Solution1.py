# Neetcode.io solution

# Time complexity: O(n) - iterate over all nums
# Space complexity: O(n) - because you need a hashset of size n

def containsDuplicate(nums):
    hset = set()

    # iterate over nums
    for n in nums:
        # if n is in hset, it's a duplicate
        if n in hset:
            return True
        # each cycle add n to the hset
        hset.add(n)
    
    # If I finished iterating over nums and didn't return true
    # there's no duplicate
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))