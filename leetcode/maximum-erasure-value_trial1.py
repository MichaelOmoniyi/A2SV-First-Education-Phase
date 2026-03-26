class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        window = 0
        left = 0
        unique = {}

        for right in range(len(nums)):
            window += nums[right]
            unique[nums[right]] = unique.get(nums[right], 0) + 1

            while unique[nums[right]] > 1:
                window -= nums[left]
                unique[nums[left]] -= 1
                left += 1
            score = max(score, window)
        return score
        