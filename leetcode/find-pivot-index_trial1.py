class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        left, right = 0, 0

        for i in range(1, n):
            left += nums[i - 1]
            leftSum[i] = left

        for i in range(n - 2, -1, -1):
            right += nums[i + 1]
            rightSum[i] = right

        for i in range(n):
            if leftSum[i] == rightSum[i]:
                return i
        else:
            return -1