# Neetcode.io solution

# Time complexity: O(n + p) where n is the number of nodes and p the number of
#                  prerequisites
# Space complexity: O(n) we will be storing the visited nodes in a hashset to
#                   prevent loops

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to prerequisite list
        # For every course we are mapping it to an empty list
        preMap = {i: [] for i in range(numCourses)}
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Stores all the courses along the current dfs path
        visiting = set()

        def dfs(crs):
            # If the course is already in the visited set, it means we found a loop
            # so we return false as we will never fulfill the prerequisites
            if crs in visiting:
                return False
            # If the course doesn't have any prerequisites (could be that it didn't
            # have any from the beginning, or that we removed it when we fulfilled it)
            # we can return True
            if preMap[crs] == []:
                return True

            # Add the current course to the visiting set to detect if we have a loop
            # later on
            visiting.add(crs)

            # Iterate over the prerequisites (which are like the neighbors of the node)
            for pre in preMap[crs]:
                # Run dfs from each neighbor. If any call returns false, it means we
                # reached a loop, so we return False
                if not dfs(pre):
                    return False

            # After finishing the dfs of the neighbors, we can remove the current course
            # from the hashset so we can use it again in another dfs run
            visiting.remove(crs)

            # If we didn't find any loops, and iterated over all the neighbors, it means
            # this course can be completed, so we will map the prerequisites to an empty list
            # so the next time we run dfs through this node, we return True from the first
            # condition and don't have to rerun again dfs from the neighbors of this node
            preMap[crs] = []

            # If we never got a false from the dfs, it means this course can be completed
            # so we can return True
            return True

        # Run dfs from all the courses we have. We are doing this in case the graph is not
        # fully connected. We will not have to redo tasks as we are changing the preMap to an
        # empty list when we complete the requisites of a course, but if we only run dfs from
        # the starting node, we could be skipping some nodes that are not connected to the
        # first node
        for c in range(numCourses):
            # If any of the courses returns False, we return False
            if not dfs(c):
                return False
        # Else, we can return True
        return True
