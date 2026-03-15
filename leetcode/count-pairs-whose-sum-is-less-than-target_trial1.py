class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # print(nums)
        start, end, count = 0, len(nums) - 1, 0

        while start < end:
            while end > start:
                if (nums[start] + nums[end]) < target:
                    count += 1
                end -= 1
            start += 1
            end = len(nums) - 1
        return count