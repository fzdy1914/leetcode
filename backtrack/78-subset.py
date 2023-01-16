class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(remain, path):
            result.append(path)

            for i in range(len(remain)):
                new_path = path.copy()
                new_path.add(remain[i])
                # careful about the remaining choice can make
                backtrack(remain[i+1:], new_path)

        backtrack(nums, set())
        return list(result)
