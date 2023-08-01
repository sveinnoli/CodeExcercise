from collections import Counter, defaultdict
# Over engineered solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        c = defaultdict(lambda: False, Counter(nums))
        for k in c:
            difference = target-k
            if (c[difference]):
                if difference == k:
                    if (c[k] > 1):
                        first = nums.index(k)
                        second = nums[first+1::].index(k)+first+1
                        return [first, second] 
                else:
                    return [nums.index(k), nums.index(difference)]

# More optimal solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found